from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required
from home.obervaciones_lab import OrdenLaboratorios
from django.contrib import messages

def login_view(request):
    return render(request, 'login.html')
@login_required
def home_view(request):
    return render(request, 'home.html')


def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            tipo_identificacion = form.cleaned_data['tipo_identificacion']
            numero_id = form.cleaned_data['numero_id']
            fecha_nac = form.cleaned_data['fecha_nac']
            user = authenticate(request, tipo_identificacion=tipo_identificacion, numero_id=numero_id, fecha_nac=fecha_nac)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales invalidas')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})






