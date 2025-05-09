from django.urls import path
from . import views


urlpatterns = [
    path('consultas/', views.menuDoctor),
    path('consultas/pacientes/', views.pacientes, name='pacientes'),
    path('consultas/paciente/<int:paciente_id>/', views.consultaPaciente, name='consulta_paciente'),
    path('consultas/paciente/<int:paciente_id>/editar/', views.editar_paciente, name='editar_paciente'),
    path('consultas/paciente/<int:paciente_id>/', views.consultaPaciente, name='consulta_paciente'),
    path('perfil/', views.perfil_paciente, name='perfil_paciente'),
]