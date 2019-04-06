from django.db import models

# Create your models here.

class Gerant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    adresse = models.CharField(max_length=100, verbose_name="Adresse")
    tel = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return "{} {}".format(self.prenom, self.nom)

class Produit(models.Model):
    libelle = models.CharField(max_length=100, verbose_name="Libellé")
    description = models.TextField(verbose_name="Description")
    prix = models.IntegerField()
    quantite = models.IntegerField()
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)


    def __str__(self):
        return "{}".format(self.libelle)

class Categorie(models.Model):
    libelle = models.CharField(max_length=100, verbose_name="Libellé")

    def __str__(self):
        return self.libelle
