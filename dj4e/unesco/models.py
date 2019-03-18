from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name

class States(models.Model) :
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name
    
class Region(models.Model) :
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name
    
class Iso(models.Model) :
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    iso = models.ForeignKey(Category, on_delete=models.CASCADE)



def __str__(self) :
    return self.name