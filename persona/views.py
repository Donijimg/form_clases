from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonaForm

# from .models import


def index(request):
  if request.method == 'POST':
    form=PersonaForm(request.POST)
    if form.is_valid():
      form.save()
      return render (request, 'index.html',{
        'form':form,})
  else:
    form = PersonaForm()
    return render (request, 'index.html', {
      'form': form
    })