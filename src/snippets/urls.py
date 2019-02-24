from django.urls import path, include

from rest_framework.routers import DefaultRouter

from snippets import views


router = DefaultRouter()

#Create a router and register our viewsets with it.
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


#The API urls are now determined automaticaly by the router
urlpatterns = [
	path('', include(router.urls)),
]



