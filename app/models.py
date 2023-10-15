from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    biography = models.TextField()  # Champ de texte pour la biographie de l'auteur
    website = models.URLField()      # Champ URL pour le site web de l'auteur
    active = models.BooleanField(default=0)   # Champ booléen pour indiquer si l'auteur est actif ou non

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)     # Champ pour le genre du livre
    ISBN = models.CharField(max_length=20)       # Champ pour le numéro ISBN du livre
    rating = models.DecimalField(max_digits=3, decimal_places=2,null=True)  # Champ pour la notation du livre

    def __str__(self):
        return self.title
