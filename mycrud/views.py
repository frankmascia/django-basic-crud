from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

# ListCreateAPIView provides GET and POST methods for the Todo model
class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH, DELETE for a specific Todo
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


