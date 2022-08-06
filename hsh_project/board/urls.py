from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>/', views.board_detail) # 뒤에 있는 pk 값이 board_detail 의 pk 값으로 들어감
]