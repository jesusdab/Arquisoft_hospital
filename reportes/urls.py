from django.urls import path
from . import views


urlpatterns = [
    path('paciente/<int:paciente_id>/', views.consultaPaciente, name='consulta_paciente'),
]