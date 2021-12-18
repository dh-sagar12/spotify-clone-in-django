from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .forms import UserCreationForm, UserChangeForm
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'is_active', 'is_staff', 'is_superuser', 'email', 'first_name', 'last_name')
    search_fields =  ('id', 'email', 'username', 'first_name', 'last_name')
    add_form = UserCreationForm
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_artist', 'is_verify', 'is_superuser', 'groups', 'user_permissions')}),
        ('Personal Information', {'fields': ('avatar', 'first_name', 'last_name', 'gender', 'date_of_birth', 'country', 'about' ), }),
        ('Other Information', {'fields': ('insta_link', 'facebook_link', 'twitter_link', 'youtube_link')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
