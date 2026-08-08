from django.db import models

class Membros(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    telefone = models.IntegerField(null=True, blank=True)
    data_ingresso = models.DateField(null=True, blank=True)

    def __str__(self):  # ← CORRIGIDO: esta linha deve estar indentada dentro da classe
        return f"{self.firstname} {self.lastname}"