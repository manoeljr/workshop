from django.db import models


class Base(models.Model):
    criados = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    __tablename__ = 'clientes'
    nome = models.CharField('NOME', max_length=150)
    email = models.CharField('EMAIL', max_length=100)
    telefone = models.CharField('TELEFONE', max_length=11)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
     