from django.db import models

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