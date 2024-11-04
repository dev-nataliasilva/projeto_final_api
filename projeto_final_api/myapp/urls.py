from django.urls import path
from .views import double_number
from .views import receive_color_objects

urlpatterns = [
    path('double/', double_number, name='double_number'),
    path('receive-colors/', receive_color_objects, name='receive_color_objects'),
]
