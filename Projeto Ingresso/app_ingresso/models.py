from django.contrib.auth.models import User
from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome' , max_length=128)
    email = models.EmailField('E-mail', blank=True, null=True)

    def str(self):
        return self.nome

class PessoaFisica(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=15)

    def str(self):
        return self.cpf


class Evento(models.Model):
    realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=128)
    sigla = models.CharField('Sigla', max_length=128)
    data_inicio = models.DateField('Data de início', blank=True, null=True)
    descricao = models.TextField()


    def str(self):
        return self.nome


class Ingresso(models.Model):
    descricao = models.CharField('Descrição', max_length=128, blank=True, null=True)
    valor = models.FloatField('Valor', blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def str(self):
        return self.descricao

class Inscricao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE)
