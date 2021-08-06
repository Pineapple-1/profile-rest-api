from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter
"""For ViewSets use Routers"""

routers = DefaultRouter()
routers.register('viewset',views.HeloViewSet,basename= 'viewset')

urlpatterns = [
    path('apiview/',views.HelloApiView.as_view()),
    path('',include(routers.urls))
]

