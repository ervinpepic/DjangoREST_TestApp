from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
		Custom permissions to allow only owner of snippet to edit or delete it
	"""

	def has_object_permission(self, request, view, obj):
		#read permssions is allowed to everyone
		# so we'll always allow GET, HEAD, or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		#Write permission is allowed only to the onwer of the snippet
		return obj.owner == request.user