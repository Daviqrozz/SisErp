from django.db import models
from django.contrib.auth.models import AbstractBaseUser,Permission

from companies.models import Entreprise

class User(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class Group(models.Model):
    name = models.CharField(max_length=150)
    enterprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE)