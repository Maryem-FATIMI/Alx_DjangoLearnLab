from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

# Book Model includ a Foregin key  with author , stating that one author can have many books 5°one to many relationship,



class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
