from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookViewSet(viewsets.ModelViewSet):

    # Restrict the view to only authenticated users
    permission_classes = [permissions.IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user
    permission_class = [IsAuthenticated]





