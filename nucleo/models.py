from django.db import models

# class <nome da sua tabela>(models.Model)-para o django entrender que é uma tabela

class Colaborador(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


# EPI
# 
# 
#
# 
#