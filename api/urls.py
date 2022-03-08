from django.urls import path

from api.views import todoAPIView, DetailTodo

urlpatterns = [
    path('todo/', todoAPIView.as_view()),
    path('todo/<int:pk>/', DetailTodo.as_view())

]