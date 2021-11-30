from django.db import models
from django.utils.timezone import now
from django.conf import settings
from accounts.models import User


# Create your models here.

class Music(models.Model):
    def music_file_directory_path(instance, filename):
        return '{2}/user_{0}/{1}'.format(instance.uploader.id, filename, 'music_files')
    
    def music_cover_photo_directory_path(instance, filename):
        return '{2}/user_{0}/{1}'.format(instance.uploader.id, filename, 'music_cover_photos')

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100, default='')
    artist= models.CharField(max_length=100, default="")
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, default='music')
    music_file = models.FileField( upload_to= music_file_directory_path)
    music_cover_photo = models.ImageField(upload_to=music_cover_photo_directory_path)
    upload_date = models.DateTimeField(default=now)
    streamed= models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-upload_date']
    

    def __str__(self):
        return self.name
