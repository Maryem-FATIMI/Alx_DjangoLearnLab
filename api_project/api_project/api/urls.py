from django.contrib import admin
from django.urls import path
from .views import BookListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListAPIView.as_view(), name='book-list'),  # Maps to the BookList view
]