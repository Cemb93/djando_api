from django.db import models

# * MODELO DE VIDEO
class MenuItem(models.Model):
  title = models.CharField(max_length = 255)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.SmallIntegerField()

# * MODELO DE ACTIVIDAD
class Book(models.Model):
  title = models.CharField(max_length = 255)
  author = models.CharField(max_length = 255)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  
  # class Meta:
  #   indexes = [
  #     models.Index(fields=['price']),
  #   ]