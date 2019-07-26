from django.urls import path
from .views import home, tradutor_inteiro


urlpatterns = [
    path('', home, name='home'),
    path('<slug:inteiro>', tradutor_inteiro, name='tradutor')
]