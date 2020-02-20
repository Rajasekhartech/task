from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length= 20 , null= False , blank= False)
    salary= models.IntegerField(null=True, blank=True)
    department1 = 'dept1'
    department2 = 'dept2'
    Departments_in_Organization = [
        (department1, "depatment1"),
        (department2, "department2"),
    ]
    depatments_in_organization = models.CharField(max_length=10, choices=Departments_in_Organization,
                                                  default=department1)
    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return "{0} {1} ".format(self.user.first_name , self.user.last_name)


@receiver(post_save,sender =User)
def user_is_created(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    else:
        instance.profile.save()