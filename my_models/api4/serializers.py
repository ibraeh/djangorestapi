from rest_framework import serializers
from my_models.models import Author, Book, Publisher


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model=Author
		fields=['id', 'name']


class BookSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model=Book
		fields=['id', 'title', 'authors', 'publisher', 'publication_date']

class PublisherSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model=Publisher
		fields=['name', 'id']