from django import forms
from myplantapp.models import PlantModel


class PlantForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class DeletePlantForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


