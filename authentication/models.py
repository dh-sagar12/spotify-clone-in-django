from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import User

# Create your models here.
class VerificationToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    authentication_key = models.CharField(max_length=100)
    created_on = models.DateTimeField(default = timezone.now)
    is_valid = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username