from django.shortcuts import render

# Create your views here.
def mass_to_energy(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'physics/mass_to_energy.html')