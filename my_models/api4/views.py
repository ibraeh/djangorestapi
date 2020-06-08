from django.urls import path
from rest_framework import status, viewsets
from my_models.models import Author, Book, Publisher
from my_models.api4.serializers import AuthorSerializer, BookSerializer , PublisherSerializer

class AuthorViewSet(viewsets.ModelViewSet):
	queryset=Author.objects.all()
	serializer_class=AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset=Book.objects.all()
	serializer_class=BookSerializer

class PublisherViewSet(viewsets.ModelViewSet):
	queryset=Publisher.objects.all()
	serializer_class=PublisherSerializer