from django.db import models
from django.contrib.auth.models import User
class Usuarios(models.Model):
    celular = models.CharField(max_length = 14)
    user = models.OneToOneField(to=User, related_name='user', on_delete=models.CASCADE)
