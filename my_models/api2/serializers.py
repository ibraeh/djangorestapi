from rest_framework import serializers
from my_models.models import Publisher, Author, Book

#serializer class for Author model
class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model=Author
		fields=['salutation', 'name', 'email']