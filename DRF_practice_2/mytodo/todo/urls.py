from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.TodosAPIView.as_view()),
    path('todo/<int:pk>/', views.TodoAPIView.as_view())
]
