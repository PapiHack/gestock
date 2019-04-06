from django.db import models

# Create your models here.

class Admin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    adresse = models.CharField(max_length=100, verbose_name="Adresse")
    tel = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return "{} {}".format(self.prenom, self.nom)