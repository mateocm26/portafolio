from django.db import models

# Create your models here.
class Education(models.Model):
    institute = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)

    def __str__ (self):
        return self.institute  

class Experience(models.Model):
    company = models.CharField(max_length = 255)
    startDate = models.CharField(max_length = 255)
    endDate = models.CharField(max_length = 255)
    functions = models.CharField(max_length = 255)
    achievements = models.CharField(max_length = 255)

    def __str__ (self):
        return self.company

class Abilities(models.Model):
    abilitieName = models.CharField(max_length = 255)
    abilitieLevel = models.CharField(max_length = 255)    

    def __str__ (self):
        return self.abilitieName
