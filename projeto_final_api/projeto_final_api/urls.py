from django.urls import path, include  # Importando include

urlpatterns = [
    path('api/', include('myapp.urls')),
]
