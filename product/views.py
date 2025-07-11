from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Person

def home(request):
    return render(request, 'home.html')

def suggest_names(request):
    query = request.GET.get('term', '')
    people = Person.objects.filter(name__icontains=query)[:5]
    suggestions = list(people.values_list('name', flat=True))
    return JsonResponse(suggestions, safe=False)

def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Person.objects.create(name=name)
            return redirect('home')
    return render(request, 'add_person.html')
