from django import forms
from .models import MappingData


class MappingDataModelForm(forms.ModelForm):
    class Meta:
        model = MappingData
        fields = ('destination_point',)
