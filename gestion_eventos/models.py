from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

class RegistroEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.usuario.nombre + ' - ' + self.evento.nombre

