from rest_framework import serializers
from my_models.models import Person

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model=Person
		fields='__all__'