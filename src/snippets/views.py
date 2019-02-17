from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.

class SnippetList(APIView):
	"""
		List all snippets or create a new snippet.
	"""
	def get(self, request, format=None):
		snippets 		= Snippet.objects.all()
		serializer 		= SnippetSerializer(snippets, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
	"""
		Retrieve, Update or Delete a code snippet.
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method 	== 'GET':
		serializer 		= SnippetSerializer(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer  	= SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.methot == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

