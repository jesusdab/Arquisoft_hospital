# Generated by Django 4.2.21 on 2025-05-09 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventosMedicos', '0006_historiaclinica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historiaclinica',
            old_name='observaciones',
            new_name='alergia_medicamentos',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='diagnostico',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='tratamiento',
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='antecedentes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='condiciones_medicas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='tipo_sangre',
            field=models.CharField(default='O+', max_length=3),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('edad', models.PositiveIntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventosMedicos.paciente'),
        ),
    ]
