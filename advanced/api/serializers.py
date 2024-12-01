from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
    
    def validate(self, data):
        if (data['publication_year']) < datetime.now().year:
            raise serializers.ValidationError("the publication year must not be in the futur.")
        return data
# BookSerializer to handle the Book Model with custom validation to publication year ,

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name','books']