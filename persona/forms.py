from django.forms import ModelForm
from .models import Persona, Dni

class PersonaForm(ModelForm):
  
    class Meta:
        model=Persona
        fields=("__all__")
        model=Dni
        fields=("__all__")