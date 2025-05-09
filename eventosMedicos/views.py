from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from eventosMedicos.models import Cita
from eventosMedicos.models import HistoriaClinica
from .models import Paciente
from django.contrib.auth.decorators import login_required

def healthCheck(request):
    return HttpResponse('ok')

# Create your views here.
def agendar_cita(request):
    return render(request, 'agendar_cita.html')

def revisar_disponibilidad(request):
    return render(request, 'revisar_disponibilidad.html')

def crear_cita(request):
    if request.method == 'POST':
        print(request.POST)  # Imprime los datos enviados desde el formulario
        medico = request.POST.get('medico')
        especialidad = request.POST.get('especialidad')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        lugar = request.POST.get('lugar')
        numero_reserva = request.POST.get('numero_reserva')
        estado = request.POST.get('estado')  # Capturar el estado

        # Crear la cita en la base de datos
        Cita.objects.create(
            medico=medico,
            especialidad=especialidad,
            fecha=fecha,
            hora=hora,
            lugar=lugar,
            numero_reserva=numero_reserva,
            estado=estado  # Guardar el estado
        )
        return redirect('/servicios')  # Redirigir a la página de servicios después de guardar
    return render(request, 'crear_cita.html')

def manejar_citas(request):
    return render(request, 'manejar_citas.html')

def consultar_citas(request):
    return render(request, 'consultar_citas.html')

def consultar_historial(request):
    return render(request, 'consultar.html')

def resultados_laboratorio(request):
    return render(request, 'resultados.html')

def telemedicina(request):
    return render(request, 'telemedicina.html')

def vacunacion(request):
    return render(request, 'vacunacion.html')

def atencion_domiciliaria(request):
    return render(request, 'domi.html')

def consultar(request):
    return redirect('/reportes/consultas/pacientes/')

def perfil_paciente(request):
    # Obtiene el paciente autenticado
    paciente = get_object_or_404(Paciente, usuario=request.user)

    # Obtiene la historia clínica asociada al paciente autenticado
    historias_clinicas = HistoriaClinica.objects.filter(paciente=paciente)

    return render(request, 'perfil_paciente.html', {
        'paciente': paciente,
        'historias_clinicas': historias_clinicas
    })