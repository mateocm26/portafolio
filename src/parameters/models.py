from django.db import models

# Create your models here.
class Etnic(models.Model):
    nameEtnic = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nameEtnic

class TypeUser(models.Model):
    userName = models.CharField(max_length = 50)

    def __str__ (self):
        return self.userName


class DocumentType(models.Model):
    nameType = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nameType

class StatusMarital(models.Model):
    nameMaritalStatus = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nameMaritalStatus

class TypeStudies(models.Model):
    nameStudiesType = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nameStudiesType

class TypeAchievements(models.Model):
    nameAchievementsType = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nameAchievementsType

class TypePosition(models.Model):
    namePositionType = models.CharField(max_length = 50)

    def __str__ (self):
        return self.namePositionType






