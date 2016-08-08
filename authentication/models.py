from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class UserAccountManager(BaseUserManager):
    # creating reader
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('invalid (or blank) email address.')
        if not kwargs.get('username'):
            raise ValueError('invalid (or blank) username.')

        account = self.model(
            email = self.normalize_email(email), username = kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    # creating writer
    # def create_writer(self,

    # creating admin
    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_admin=True
        account.save()
        return account



class UserAccount(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)

    first_name = models.CharField(max_length=20, blank=True, default="firstnameherp")
    last_name = models.CharField(max_length=20, blank=True, default="lastnamederp")
    # birth_date = models.DateField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    bio_short = models.CharField(max_length=140, blank=True, default="default short bio")
    bio_long = models.CharField(max_length=500, blank=True, default="default long bio")
    company = models.CharField(max_length=50, default="default company")

    is_reader = models.BooleanField(default=True)
    is_writer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
