from django.urls import path
from . import views
from rest_framework import routers
from .views import TodosAPIViewsets

router = routers.SimpleRouter()
router.register('todo', TodosAPIViewsets)

urlpatterns = router.urls

# urlpatterns = [
#     path('todo/', views.TodosAPIView.as_view()),
#     path('generics/todo/', views.TodosAPIGenerics.as_view()),
#     path('mixin/todo/', views.TodosAPIMixins.as_view()),
#     path('todo/<int:pk>/', views.TodoAPIView.as_view()),
#     path('generics/todo/<int:pk>/', views.TodoAPIGenerics.as_view()),
#     path('mixin/todo/<int:pk>/', views.TodoAPIMixins.as_view()),
#     path('done/', views.DoneTodosAPIView.as_view()),
#     path('generics/done/', views.DoneTodosAPIGenerics.as_view()),
#     path('mixin/done/', views.DoneTodosAPIView.as_view()),
#     path('done/<int:pk>/', views.DoneTodoAPIMixins.as_view()),
#     #path('generics/done/<int:pk>/', views.DoneTodoAPIGenerics.as_view()),
#     path('mixin/done/<int:pk>/', views.DoneTodoAPIMixins.as_view()),

# ]
