from django.db import models

# Create your models here.

class studio_calendar(models.Model):
    Owner_name=models.CharField(max_length=120)
    Studio_name=models.CharField(max_length=120, null=True, blank=True)
    Teacher_name=models.CharField(max_length=120, null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    Operate_From=models.DateTimeField(auto_now=False,auto_now_add=False)
    Operate_To=models.DateTimeField(auto_now=False,auto_now_add=False)
    Hourly_rate=models.DecimalField(max_digits=10,decimal_places=2,null=True,default=0.00)


    def __str__(self):
        return self.Studio_name

class user_calendar(models.Model):
    studio=models.ForeignKey('studio_calendar', on_delete=models.CASCADE)
    User_name=models.CharField(max_length=120)
    Date=models.DateField(auto_now=False,auto_now_add=False,null=True)
    User_booked_from=models.TimeField(auto_now=False,auto_now_add=False)
    User_booked_to=models.TimeField(auto_now=False,auto_now_add=False)
    User_actually_from=models.TimeField(auto_now=False,auto_now_add=False)
    User_actually_to=models.TimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.User_name
