from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class CreateUserSerializer(serializers.ModelSerializer):
    # email      = serializers.SerializerMethodField()
    first_name = serializers.CharField(max_length=255,)
    last_name  = serializers.CharField(max_length=255,)
    # mobileNo   = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email','password','first_name','last_name','mobileNo','address','is_staff','is_superuser','is_active','is_admin')
        extra_kwargs = {
            'first_name' : {'required' : True},
            'last_name'  : {'required' : True},
            'mobileNo'   : {'required' : True},
            'address'    : {'required' : True},

        }


    def validate_first_name(self,first_name):
        if first_name.isalpha():
            return first_name
        else:
            raise serializers.ValidationError("The name shouldn't contain numbers or special characters")

    def validate_last_name(self,last_name):
        if last_name.isalpha():
            return last_name
        else:
            raise serializers.ValidationError("The name shouldn't contain special characters")

    
    def create(self, validated_data):
        data = validated_data.copy()
        del data['email']
        del data['password']
        print(data)
        user = User.objects.create_user(validated_data['email'],validated_data['password'],**data)
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','email', 'is_active', 'first_name', 'last_name', 'mobileNo','address','is_staff','is_superuser','is_admin']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style = { 'input_type': 'password'}, trim_whitespace = False
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            email = email.lower()
            if User.objects.filter(email = email).exists():
                test = User.objects.filter(email = email).first()
                print(test.check_password(password))
                print(email, password)
                user = authenticate(request = self.context.get('request'), email = email, password = password)
                print(user)

            else:
                msg = {
                    'message' : 'Email not found',
                    'status' : False,
                }    
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'message' : 'Email and password not matching. Try again',
                    'status' : False,
                }    
                raise serializers.ValidationError(msg)
        else:
            msg = {
                    'message' : 'Email and password not found in request',
                    'status' : False,
                }    
            raise serializers.ValidationError(msg)
        
        
        data['user'] = user
        return data