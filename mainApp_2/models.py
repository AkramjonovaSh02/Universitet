from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField()

class Fan(models.Model):
    nom = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField()

class Ustoz(models.Model):
    ism = models.CharField(max_length=50)
    jins = models.CharField(max_length=10, choices=(
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    ))
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=15, choices=(
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr')
    ))
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

