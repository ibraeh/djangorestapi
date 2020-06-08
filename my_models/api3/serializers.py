from rest_framework import serializers
from my_models.models import Author

class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model=Author
		fields='__all__'