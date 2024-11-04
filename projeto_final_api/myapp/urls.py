from django.urls import path
from .views import receive_color_objects

urlpatterns = [
    path('receive-colors/', receive_color_objects, name='receive_color_objects'),
]
