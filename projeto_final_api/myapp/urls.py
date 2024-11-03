from django.urls import path
from .views import double_number

urlpatterns = [
    path('double/', double_number, name='double_number'),
]
