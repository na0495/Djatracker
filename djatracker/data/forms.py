from django import forms
from .models import store


class StoreModelForm(forms.ModelForm):
    class Meta:
        model = store
        fields = ('destination_point',)
