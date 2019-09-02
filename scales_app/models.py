from django.db import models

# Create your models here.

class Fretboard(models.Model):

    # User specifies the particular major scale they would like.
    scale = models.CharField(max_length=3)

    # User specifies the tuning of each string on their guitar.
    #Largest diameter string is string 1. A traditionally tunded guitar would be as follows 1=E, 2=A, 3=D, 4=G, 5=B, 6=E

    string1 = models.CharField(max_length=3)
    string2 = models.CharField(max_length=3)
    string3 = models.CharField(max_length=3)
    string4 = models.CharField(max_length=3)
    string5 = models.CharField(max_length=3)
    string6 = models.CharField(max_length=3)