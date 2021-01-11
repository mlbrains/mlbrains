from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MlClient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    Client_name = models.CharField(max_length=100, null=True, blank=True)
    Client_email = models.CharField(max_length=100, null=True, blank=True)
    Client_phone = models.CharField(max_length=100, null=True, blank=True)
    Client_address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Client_name