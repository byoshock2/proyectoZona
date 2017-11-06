from django.db import models
from django.contrib import admin

class Arbitro(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha = models.DateField()
    def __str__(self):
        return self.nombre

class Partido(models.Model):
    nombre    = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    fecha = models.DateField()
    arbitros   = models.ManyToManyField(Arbitro, through='Agenda')
    def __str__(self):
        return self.nombre

class Agenda(models.Model):
    Arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    Partido = models.ForeignKey(Partido, on_delete=models.CASCADE)

class AgendaInLine(admin.TabularInline):
    model = Agenda
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class ArbitroAdmin(admin.ModelAdmin):
    inlines = (AgendaInLine,)
