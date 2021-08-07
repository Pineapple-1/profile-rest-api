from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter
"""For ViewSets use Routers"""

routers = DefaultRouter()
routers.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
