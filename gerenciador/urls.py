from django.urls import path
from gerenciador.views import index


urlpatterns = [
    path('', index, name='index'),
]
