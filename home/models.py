from django.db import models


class Pontuacoe(models.Model):
    nome = models.CharField(max_length=30)
    pontos = models.IntegerField()

    def __str__(self):
        return self.nome
