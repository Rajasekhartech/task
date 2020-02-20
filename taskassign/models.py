from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tasks(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null= True, blank = True)
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class assined_task(models.Model):
    task = models.IntegerField(null= True, blank= True)
    emp = models.IntegerField(null= True, blank= True)
    assigned_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=False, null=True)
