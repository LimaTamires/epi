from django.db import models

class Setor(models.Model):
    id_setor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Colaborador(models.Model):
    nome = models.CharField(max_length=45, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    status = models.BooleanField(null=True, blank=True)
    #setor = models.ForeignKey(
    #    Setor,
    #    on_delete=models.PROTECT,
    #    related_name='colaboladores'
    #
    
    def __str__(self):
        return self.nome


# EPI
# 
# 
#
# 
#