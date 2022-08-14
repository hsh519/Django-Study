from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloAPI),
    path('books/', views.booksAPI),
    path('book/<int:bid>/', views.bookAPI)
]