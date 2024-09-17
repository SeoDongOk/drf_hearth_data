from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
