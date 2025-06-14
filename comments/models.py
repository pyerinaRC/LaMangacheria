from django.db import models

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()  # Comentario largo
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor}: {self.contenido[:30]}"

