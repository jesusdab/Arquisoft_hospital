from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HistoriaClinica(models.Model):
    paciente = models.ForeignKey('usuarios.Paciente', on_delete=models.CASCADE, related_name='historias_clinicas')
    tipo_sangre = models.CharField(max_length=10, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    alergia_medicamentos = models.TextField()
    antecedentes = models.TextField()
    condiciones_medicas = models.TextField()
    

