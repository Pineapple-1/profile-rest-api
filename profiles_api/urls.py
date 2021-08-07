from django.contrib.auth import login
from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter
"""For ViewSets use Routers"""

routers = DefaultRouter()
routers.register('profile', views.UserProfileViewSet)
routers.register('feed', views.ProfileFeedItemViewSet)



urlpatterns = [
    path('login/', views.UserLoginApiView.as_view(),name='login'),
    path('', include(routers.urls))
]
