# pessoas/models.py
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=50, choices=[
        ('contabilidade', 'Contabilidade'),
        ('financeiro', 'Financeiro'),
        ('atendimento', 'Atendimento'),
        ('orcamento', 'Orçamento'),
        ('ti', 'TI')
    ])
    email = models.EmailField()

    def __str__(self):
        return self.nome
