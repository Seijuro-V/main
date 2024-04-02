from django.shortcuts import render
from django.http import JsonResponse
from .utils import generate_lotto_numbers
from .models import LottoDraw

# Create your views here.

def generate_lotto_draw(request):
    numbers = generate_lotto_numbers()
    LottoDraw.objects.create(numbers=numbers)
    return JsonResponse ({'numbers': numbers})