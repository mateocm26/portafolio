from django.db import models

# Create your models here.
class UserName(models.Model):
    userName = models.CharField(max_length = 255)
    userLastname = models.CharField(max_length = 255)
    UserEmail = models.CharField(max_length = 255)
    userPass = models.CharField(max_length = 255)
    userStatus = models.CharField(max_length = 45)


    def __str__(self):
        return self.userName

class DataUser(models.Model):
    userGender = models.CharField(max_length = 45)
    perfilPro = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 45)
    adress = models.CharField(max_length = 255)
    

    def __str__(self):
        return self.userGender
