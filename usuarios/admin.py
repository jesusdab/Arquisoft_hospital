from django.contrib import admin
from .models import Usuario, Paciente, Doctor, Enfermero, Tecnico, ProfesionalSalud, Project, Task
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Enfermero)
admin.site.register(Tecnico)
admin.site.register(ProfesionalSalud)

