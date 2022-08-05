from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    wikipedia = models.URLField(blank=True)

    def affichage_nom_prenom(self):
        return(f"{self.firstname} {self.lastname}")


class Book(models.Model):
    Categories = [("Aventure","Aventure"),("Fantastique","Fantastique"),("Thriller","Thriller"),("Romance","Romance")
        ,("Horreur","Horreur"),("Science-fiction","Science-fiction")]
    title = models.CharField(max_length=100)
    price = models.DecimalField(blank=True,decimal_places=2,max_digits=100)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True,null=True) ##on_delete : paramètre le champ author des livres d'un auteur
    category = models.CharField(max_length=50,choices=Categories)               #si ce dernier est supprimé du modèle Author
    stock = models.IntegerField(default=0)

    def affichage_titre(self):
        return self.title