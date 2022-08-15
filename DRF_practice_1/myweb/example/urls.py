from django.urls import path
from rest_framework import routers
from .views import BookViewset

router = routers.SimpleRouter()
router.register('books', BookViewset)
urlpatterns = router.urls
    # path('hello/', views.HelloAPI),
    # path('books/', views.booksAPI),
    # path('book/<int:bid>/', views.bookAPI),
    # path('mixin/books/', views.BooksAPIMixins.as_view()),
    # path('mixin/book/<int:bid>/', views.BookAPIMixins.as_view()),
    # path('generics/books/', views.BooksAPIGenerics.as_view()),
    # path('generics/book/<int:bid>/',views.BookAPIGenerics.as_view())
