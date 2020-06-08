from my_models.api2.serializers import AuthorSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_models.models import Author


@api_view(['GET','POST'])
def author_list(request, format=None):
	#list all authors
	if request.method == "GET":
		aut=Author.objects.all()
		serializer=AuthorSerializer(aut, many=True)
		return Response(serializer.data)

	elif request.method=="POST":
		serializer=AuthorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def author_detail(request, pk, format=None):
	try:
		aut=Author.objects.get(pk=pk)
	except Author.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	#Retrieving a detail record from Authors
	if request.method=='GET':
		serializer=AuthorSerializer(aut)
		return Response(serializer.data)

	elif request.method=='PUT':
		serializer=AuthorSerializer(aut, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_PARTIAL_CREATED)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

	elif request.method=='DELETE':
		aut.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


############################################################
#Class-based api view
