from django.urls import path
from .views import generate_lotto_draw

urlpatterns = [
    path('draw/', generate_lotto_draw, name='generate_lotto_draw'),
]
