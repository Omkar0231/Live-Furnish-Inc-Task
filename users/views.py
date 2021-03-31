from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from knox.views import LoginView as KnoxLoginView
from rest_framework.generics import CreateAPIView,RetrieveAPIView

#models
from .models import User

#For LoginView
from .serializer import LoginSerializer, CreateUserSerializer
from django.contrib.auth import login



class SignUp(CreateAPIView):
    permission_classes = [~IsAuthenticated]
    serializer_class   = CreateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'user':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serializer.errors},status.HTTP_400_BAD_REQUEST)
            


class LoginAPI(KnoxLoginView,CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            
        return Response(response.data,status=status.HTTP_200_OK) 