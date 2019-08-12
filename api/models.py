from django.db import models

# Create your models here.

class Escalas(models.Model):

    class Meta:
        db_table = "Escalas"

    vendedor = models.CharField(max_length=5)
    periodo  = models.CharField(max_length=10)
    valor    = models.CharField(max_length=10)

    def __str__(self):
        return self.vendedor
