from django.contrib.auth.models import User


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, renderers, viewsets


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
	"""
		This viewset automaticaly provide retrieve, list, create, update, destroy actions
	"""
	queryset 			= Snippet.objects.all()
	serializer_class 	= SnippetSerializer
	permission_classes 	= (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
		This model automaticaly provide list and detail actions
	"""
	queryset 			= User.objects.all()
	serializer_class 	= UserSerializer



