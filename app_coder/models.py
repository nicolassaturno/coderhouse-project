from django.db import models


class Seed(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    specimen = models.CharField(max_length=40)
    taste = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} seed --'


class Insurance(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'Producto {self.name} --'


class Pipes(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
  

    def __str__(self):
        return f'Bongs: {self.name} tipo: {self.model} --'


