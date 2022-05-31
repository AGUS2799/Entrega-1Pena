from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=40)
    n_category = models.IntegerField()

    def __str__(self):
        return f'Categoria: {self.category}'


class Winners(models.Model):
    name_couple = models.CharField(max_length=40)


    def __str__(self):
        return f'Nombres de los ganadores: {self.name_couple}'


class Players(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre del Jugador: {self.name} {self.last_name} -- Posición: {self.position} --'


