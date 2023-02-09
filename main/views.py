# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
# Create your views here.
from .models import Book
from .serializerd import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteUpdateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

