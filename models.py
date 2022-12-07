from django.db import models

class Emprestimo(models.Mol):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    
