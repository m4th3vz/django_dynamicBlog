from django.db import models

class Text(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='text_images/', blank=True, null=True)

    def __str__(self):
        return self.titulo
