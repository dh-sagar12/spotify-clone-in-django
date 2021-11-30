from django.contrib import admin
from home.models import Music


# Register your models here.
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist', 'genre')
