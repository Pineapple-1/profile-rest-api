from profiles_api import views
from django.urls import path
from profiles_api import views

urlpatterns = [
    path('helo/',views.HelloApiView.as_view())
]

