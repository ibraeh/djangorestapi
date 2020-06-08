from rest_framework import status
from rest_framework.response import Response
from my_models.models import Author
from my_models.api3.serializers import AuthorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import permissions #permissions
from rest_framework.authentication import BasicAuthentication


#generic class based 
from rest_framework import generics

class AuthorList(APIView):
	#List all authors
	def get(self, request, format=None):
		aut=Author.objects.raw('SELECT id, name FROM my_models_author') #filter(salutation='Miss') 
		serializer=AuthorSerializer(aut, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer=AuthorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED_SUCCESSFULLY)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
	def get_object(self, pk):
		try:
			return Author.objects.get(pk=pk)
		except Author.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		aut=self.get_object(pk)
		serializer=AuthorSerializer(aut)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		aut=self.get_object(pk)
		serializer=AuthorSerializer(aut)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		aut=self.get_object(pk)
		aut.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

######################################################################
# Generic class based

class AuthorGenericList(generics.ListCreateAPIView):
	queryset=Author.objects.all() #raw('SELECT id, name FROM my_models_author')
	serializer_class=AuthorSerializer
	
	# authentication_classes=[BasicAuthentication]
	# permission_classes=(permissions.IsAuthenticated,) #permissions

class AuthorGenericDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Author.objects.all()
	serializer_class=AuthorSerializer

	#authentication_classes=[BasicAuthentication]
	#permission_classes=[permissions.IsAuthenticated] #permissions

	#lookup_field = 'pk'