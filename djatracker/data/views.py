from django.shortcuts import render, get_object_or_404
from .models import store
from .forms import StoreModelForm

# Create your views here.


def calculate_distance_view(request):
    object = get_object_or_404(store, id=1)
    form = StoreModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.destination_point = form.cleaned_data.get('destination_point')
        instance.location = 'Tangier'
        instance.distance = 350,
        instance.save()
    context = {
        'distance': object,
        'form': form,
    }
    return render(request, 'data/main.html', context)
