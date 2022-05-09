from django.urls import path
from .views import home, about, simulation, resultat

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('simulation', simulation, name='simulation'),
    path('resultat', resultat, name='resultat'),
]
