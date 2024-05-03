from django.urls import path

from .views import home

app_name = 'home'
urlpatterns = [
    path('', view=home, name='home')
]