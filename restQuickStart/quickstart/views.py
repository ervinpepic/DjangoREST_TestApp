from django.contrib.auth.models import User, Group

from rest_framework import viewsets

from quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
	"""
		API endpoints that allows user to be viewed or edited.
	"""
	queryset			= User.objects.all().order_by('-date_joined')
	serializer_class 	= UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
		API endpints that allow groups to be viewed or edited.
	"""

	queryset 			= Group.objects.all()
	serializer_class	= GroupSerializer
