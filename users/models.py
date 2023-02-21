from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    name = models.CharField(max_length=50, blank=False)
    member_numbers = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    



class Profile(models.Model):

    POSITION_CHOICES = [
        ("0","Father"),
        ("1","Mother"),
        ("2","Son"),
        ("3","Daughter"),
        ("4","Sister"),
        ("5","Brother"),
        ("6","Husband"),
        ("7","Wife"),
        ("8","None"),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    has_a_family = models.BooleanField(default=False)
    is_head = models.BooleanField(default=False)
    family = models.ForeignKey(Family, on_delete=models.DO_NOTHING, blank=True, null=True)
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
    
