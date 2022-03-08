from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import TodoSerializer
from todos.models import TodoModel


class todoAPIView(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
