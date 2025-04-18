from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f"({self.id}){self.descricao}"