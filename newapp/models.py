from django.db import models

# Create your models here.


class Gateway(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    ip_addresses = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Route(models.Model):
    prefix = models.CharField(max_length=200)
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
