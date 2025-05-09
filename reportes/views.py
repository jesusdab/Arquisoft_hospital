from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import HistoriaClinica
from django.shortcuts import render, get_object_or_404
from usuarios.models import Paciente

from .utils import retry_operation
# Create your views here.

@retry_operation(max_retries=5, delay=2, exponential_backoff=True)
def consultaPaciente(request, paciente_id):
    try:
        
        #consultaPaciente: Vista para consultar la historia clínica de un paciente.
        # Obtener el paciente por su ID
        paciente = get = get_object_or_404(Paciente, id=paciente_id)
        historiaClinica = paciente.historias_clinicas.all()
        
        data = {
            'paciente': paciente,
            'historiaClinica': historiaClinica,
        }

        return render(request, 'consultaPaciente.html', data)
    except Exception as e:
        # Manejo de errores
        return JsonResponse({'error': str(e)}, status=500)
    
def menuDoctor(request):
    nombreDoc = request.user.username
    # Renderizar la plantilla del menú del doctor
    return render(request, 'menuConsulta.html')

def pacientes(request):
    # Obtener todos los pacientes
    pacientes = Paciente.objects.all()
    
    # Renderizar la plantilla con la lista de pacientes
    return render(request, 'pacientes.html', {'pacientes': pacientes})


def editar_paciente(request, paciente_id):
    # Obtiene el paciente por su ID
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        # Actualiza los datos del modelo User relacionado
        paciente.usuario.first_name = request.POST.get('nombre')  # Usa first_name para el nombre
        paciente.usuario.save()  # Guarda los cambios en el modelo relacionado

        # Actualiza los datos del modelo Paciente
        paciente.email = request.POST.get('email')
        paciente.edad = request.POST.get('edad')
        paciente.telefono = request.POST.get('telefono')
        paciente.save()  # Guarda los cambios en el modelo Paciente

        return redirect('consulta_paciente', paciente_id=paciente.id)  # Redirige a la página de consulta del paciente

    return render(request, 'editar_paciente.html', {'paciente': paciente})

def perfil_paciente(request):
    # Obtiene el paciente autenticado
    paciente = get_object_or_404(Paciente, usuario=request.user)

    # Obtiene la historia clínica asociada al paciente autenticado
    historias_clinicas = HistoriaClinica.objects.filter(paciente=paciente)

    return render(request, 'perfil_paciente.html', {
        'paciente': paciente,
        'historias_clinicas': historias_clinicas
    })