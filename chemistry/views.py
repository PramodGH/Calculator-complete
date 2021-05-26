from django.shortcuts import render, HttpResponse


def atomic_mass(request):
    return render(request, 'chemistry/base.html')
