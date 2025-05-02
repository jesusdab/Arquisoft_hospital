from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import HistoriaClinica
from django.shortcuts import render, get_object_or_404
from usuarios.models import Paciente
# Create your views here.

def consultaPaciente(request, paciente_id):
    
    #consultaPaciente: Vista para consultar la historia clínica de un paciente.
    
    # Obtener el paciente por su ID
    paciente = get = get_object_or_404(Paciente, id=paciente_id)
    historiaClinica = paciente.historias_clinicas.all()
    
    data = {
        'paciente': paciente,
        'historiaClinica': historiaClinica,
    }

    return render(request, 'consultaPaciente.html', data)