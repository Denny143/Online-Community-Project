from django.db import models

# Create your models here.

class studio_calendar(models.Model):
    name=models.CharField(max_length=120)
    studio=models.CharField(max_length=120, null=True, blank=True)
    teacher=models.CharField(max_length=120, null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    From=models.DateTimeField(auto_now=False,auto_now_add=False)
    To=models.DateTimeField(auto_now=False,auto_now_add=False)


    def __str__(self):
        return self.name
