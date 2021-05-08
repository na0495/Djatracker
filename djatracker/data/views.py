from django.shortcuts import render, get_object_or_404
from .models import store

# Create your views here.


def calculate_distance_view(request):
    object = get_object_or_404(store, id=1)
    context = {
        'distance': object
    }
    return render(request, 'store/main.html', context)
