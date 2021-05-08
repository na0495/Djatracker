from django.shortcuts import render, get_object_or_404
from .models import MappingData
from .forms import MappingDataModelForm

# Create your views here.


def calculate_distance_view(request):
    object = get_object_or_404(MappingData, id=1)
    form = MappingDataModelForm(request.POST or None)

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
