from django.db import models

class Text(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo
