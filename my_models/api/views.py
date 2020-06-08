from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from my_models.models import Person
from my_models.api.serializers import PersonSerializer

@api_view(['GET',])
def api_detail_view(request, name):

	try: 
		pub=Person.objects.get(name=name)
	except Person.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
 			
	if request.method == "GET":
 		serializer=PersonSerializer(pub)
 		return Response(serializer.data)


#method to update records
@api_view(['PUT',])
def api_update_view(request, name):
	try:
		pub=Person.objects.get(name=name)
	except Person.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='PUT':
		serializer=PersonSerializer(pub)
		return Response(serializer.data)
