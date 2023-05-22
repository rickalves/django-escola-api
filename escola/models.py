from django.db import models

class Aluno(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False)
    matricula = models.IntegerField(null=False)
    email = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
              


class Curso(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=50, null=False)
    vagas = models.IntegerField(null=False)

    def __str__(self):
        return self.nome