from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy
import hashlib

class CustomUser(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        other_fields.setdefault('role', 'ADMIN')
        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError(gettext_lazy('Email is required'))
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('role', 'USER')
        email = self.normalize_email(email)
        #password = hashlib.md5(password.encode('utf-8')).hexdigest()
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

class UserAccount(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUser()

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'

    base_role = Role.USER

    role = models.CharField(max_length=50, default='USER', choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.name + ' ( '+self.email+' )'