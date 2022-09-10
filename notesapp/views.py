from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import notes
from .forms import TodoForm
# Create your views here.


def home(request):
    return HttpResponse("<h1>hello<h1>")


def notesapp(request):
    context = {}
    context["dataset"] = notes.objects.all()

    return render(request, 'index.html', context)


def create_notes(request):
    context = {}
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'forms.html', context)
