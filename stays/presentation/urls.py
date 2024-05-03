from django.urls import path

from .views import home, presentation_list

app_name = 'presentation'
urlpatterns = [
    path('', view=presentation_list, name='list'),
    path('<str:enrollment>/', view=home, name='home'),
]