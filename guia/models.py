from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    legajo = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} - Profesor: {self.profesor}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} - Materia: {self.materia}"