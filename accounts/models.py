from os import truncate
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.



class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username= username, **other_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_staff True')

        return self.create_user(email, username,  password, **other_fields)
    
    
class User(AbstractBaseUser, PermissionsMixin):
    def avatar_directory_path(instance, filename):
        return '{2}/user_{0}/{1}'.format(instance.id, filename, 'avatar')
    
    
    email= models.EmailField(_("email address"), max_length=254, unique=True)
    username = models.CharField(max_length=180, unique=True)
    about = models.TextField(_('about'), max_length=250, blank=True)
    avatar = models.ImageField(upload_to=avatar_directory_path,  blank=True)
    is_artist = models.BooleanField(default=False)
    date_of_birth =  models.DateField(blank=True, null=True)
    country=  models.CharField(max_length=100, blank=True)
    is_verify =  models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_name =  models.CharField(max_length=100, blank=True)
    first_name= models.CharField(max_length=100, blank=True)
    insta_link = models.URLField(max_length=500, blank=True)
    facebook_link = models.URLField(max_length=500, blank=True)
    twitter_link = models.URLField(max_length=500, blank=True)
    youtube_link = models.URLField(max_length=500, blank=True)
    external_link = models.URLField(max_length=500, blank=True)
    date_joined = models.DateTimeField(blank=True, default=timezone.now)
    
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHER = -1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'), (GENDER_OTHER, 'Other')]
    gender = models.IntegerField(choices=GENDER_CHOICES, default=None)
    
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username