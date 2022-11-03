from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=64)
    documento = models.FileField(upload_to='documento_aluno', null=True, blank=True)

    def __str__(self):
        return self.nome
