from django.db import models
  
class Dni(models.Model):
  dni = models.CharField(max_length=10, blank=False, null=False)

  def __str__(self):
      return self.dni
  
class Persona(models.Model):
  nombre = models.CharField(max_length=50, blank=False, null=False)
  apellido= models.CharField(max_length=50, blank=False, null=False)
  correo= models.EmailField()
  dni = models.ForeignKey(Dni, on_delete=models.CASCADE, related_name='Persona')
  
  def __str__(self):
      return self.nombre
  