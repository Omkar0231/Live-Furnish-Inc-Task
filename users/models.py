from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.core.validators import RegexValidator


class UserManager(BaseUserManager):

    def create_user(self,email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        print(email)
        print(password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Superuser with the given email and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser = True")
        if extra_fields.get('is_admin') is not True:
            raise ValueError("Superuser must have is_admin = True")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email         = models.EmailField(max_length=254, unique=True)
    password      = models.CharField(max_length=100,null=False)
    first_name    = models.CharField(max_length=255, null=True, blank=True)
    last_name     = models.CharField(max_length=255, null=True, blank=True)
    phone_regex   = RegexValidator(regex = r'^\+?1?\d{10}$', message ="Phone number must be entered in the format 9999999999. Only 10 digits allowed.")
    mobileNo      = models.CharField(unique=True,validators =[phone_regex], max_length=15) 
    address       = models.CharField(max_length=255, null=True, blank=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_admin      = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['mobileNo']

    objects = UserManager()

    def get_full_name(self):
        print('model method',self.first_name)
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
