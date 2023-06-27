from django.db import models
from users.models import Profile

class Costs(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    cost = models.FloatField()

    def __str__(self):
        return f'{self.title} - {self.user}'
    

    