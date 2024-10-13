from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManeger


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    #add manager to model
    objects = UserManeger()

    #phone number validation
    USERNAME_FIELD = 'phone_number'
    #related to createsuperuser
    REQUIRED_FIELDS = ['email', 'full_name']


    def __str__(self):
        return self.email
    
    

    #check if user is staff
    @property
    def is_staff(self):
        return self.is_admin
    


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}' 