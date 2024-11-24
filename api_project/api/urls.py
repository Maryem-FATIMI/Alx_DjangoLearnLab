from django.contrib import admin
from django.urls import path
from .views import BookListAPIView
from .views import BookList
from django.urls import path, include
#from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('books/', BookListAPIView.as_view(), name='book-list'),  # Maps to the BookList view
    path('api/books/', BookList.as_view(), name='books'),
 path('api-token-auth/', obtain_auth_token, name='api-token-auth')
]