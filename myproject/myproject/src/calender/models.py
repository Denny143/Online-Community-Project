from django.conf import settings
from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
            )

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    teach_from=models.DateTimeField(auto_now=False,auto_now_add=False)
    teach_to=models.DateTimeField(auto_now=False,auto_now_add=False)

    created_on=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s at %s" % (self.teacher, self.place)


class StudioUser(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,null=True
            )

    studio_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,null=True
    )

    booked_from=models.DateTimeField(auto_now=False,auto_now_add=False)
    booked_to=models.DateTimeField(auto_now=False,auto_now_add=False)

    created_on=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s at %s" % (self.studio_user, self.place)
