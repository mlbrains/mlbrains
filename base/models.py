from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MlUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    labels_selected = models.CharField(max_length=1000, null=True, blank=True, default=0)
    labels_done = models.CharField(max_length=1000, null=True, blank=True, default=0)
    labels_correct = models.CharField(max_length=1000, null=True, blank=True, default=0)
    labels_incorrect = models.CharField(max_length=1000, null=True, blank=True, default=0)

    
    def __str__(self):
        return self.name

class Projectsdetail(models.Model):
    project_ID = models.CharField(max_length=1000, null=True, blank=True)
    project_description = models.CharField(max_length=1000, null=True, blank=True)
    project_Work_type = models.CharField(max_length=1000, null=True, blank=True)
    project_points = models.CharField(max_length=1000, null=True, blank=True)
    project_status = models.BooleanField(default=False)

    def __str__(self):
        return self.project_ID

class Elements(models.Model):
    projectchoices = (
        ('project1', 'project1'),
        ('project2', 'project2'),
        ('project3', 'project3'),
    )
    #element_ID = models.IntegerField(null=True, blank=True)
    project_ID = models.CharField(max_length=100, choices=projectchoices, default=None)
    filename = models.ImageField(upload_to='images', default=None)
    def __str__(self):
        return self.project_ID
