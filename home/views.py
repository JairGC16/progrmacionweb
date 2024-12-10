from django.shortcuts import render

# Create your views here.

# Vista de Home Admin
def home(request):
    return render(request, 'Home/home_view.html')

# Vista de Home Usuario
def homeuser(request):
    return render(request, 'HomeUser/home_user_view.html')

# Vista de Historial
def historial(request):
    return render(request, 'Historial/historial_view.html')