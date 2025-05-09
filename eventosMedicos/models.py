from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EventoMedico(models.Model):
    fechas = models.DateField()
    descripcion = models.TextField()
    paciente = models.ForeignKey('usuarios.Paciente', on_delete=models.CASCADE, related_name='eventos_medicos')
    profesional_salud = models.ForeignKey('usuarios.ProfesionalSalud', on_delete=models.CASCADE, related_name='eventos_medicos')

class Cirugia(models.Model):
    evento_medico = models.ForeignKey(EventoMedico, on_delete=models.CASCADE, related_name='cirugias')
    tipo_cirugia = models.CharField(max_length=100)
    fecha_cirugia = models.DateField()
    riesgos = models.TextField()

class Preescripcion(models.Model):
    evento_medico = models.ForeignKey(EventoMedico, on_delete=models.CASCADE, related_name='prescripciones')
    medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)

class Consulta(models.Model):
    evento_medico = models.ForeignKey(EventoMedico, on_delete=models.CASCADE, related_name='consultas')
    motivo_consulta = models.TextField()
    examen_fisico = models.TextField()
    diagnostico = models.TextField()
    observaciones = models.TextField()
    
class Cita(models.Model):
    paciente = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=200, default='Consultorio General')
    numero_reserva = models.CharField(max_length=50, unique=True, default='N/A')
    estado = models.CharField(
        max_length=50,
        choices=[('pendiente', 'Pendiente'), ('confirmada', 'Confirmada')],
        default='pendiente'  # Valor predeterminado
    )

    def __str__(self):
        return f"{self.medico} - {self.especialidad} ({self.fecha} {self.hora})"
    
class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo User
    email = models.EmailField()
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario.first_name
    
class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historias_clinicas')
    tipo_sangre = models.CharField(max_length=3)
    alergia_medicamentos = models.TextField(blank=True, null=True)
    antecedentes = models.TextField(blank=True, null=True)
    condiciones_medicas = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Historia de {self.paciente.usuario.first_name} - {self.doctor.username}"

    
