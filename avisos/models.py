from django.db import models

class Aviso(models.Model):
    aviso = models.TextField(help_text="Texto del aviso")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:  
        ordering = ['-fecha_inicio', '-id']  

    def __str__(self): 
        return self.aviso[:50]
