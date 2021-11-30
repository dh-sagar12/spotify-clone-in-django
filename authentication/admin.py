from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from .models import VerificationToken


@admin.register(VerificationToken)
class VerificationTokemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'authentication_key', 'created_on', 'is_valid')