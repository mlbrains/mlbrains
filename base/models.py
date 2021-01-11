from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MlUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
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
    Total_elements = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.project_ID

class Elements(models.Model):
    statuschoices = (
        ('New', 'New'),
        ('Allocated', 'Allocated'),
        ('Labeled', 'Labeled'),
        ('Unclear', 'Unclear'),
    )
    project_ID = models.ForeignKey(Projectsdetail, on_delete=models.CASCADE, default=None)
    Allocated_to_User = models.ForeignKey(MlUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
    element_ID = models.CharField(max_length=1000,null=True)
    status = models.CharField(max_length=1000, choices=statuschoices,null=True, default=None)
    filename = models.ImageField(upload_to='images', default=None, blank=True)
    def __str__(self):
        return self.element_ID

