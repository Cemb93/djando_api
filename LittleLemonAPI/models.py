from django.db import models

class Category(models.Model):
  slug = models.SlugField()
  title = models.CharField(max_length=255)
  
  def __str__(self) -> str:
    return self.title

# * MODELO DE VIDEO
class MenuItem(models.Model):
  title = models.CharField(max_length = 255)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.SmallIntegerField()
  category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)# ? RELACION 1 - MUCHOS
  
  def __str__(self) -> str:
    return self.title

"""
  !NOTA: En la relacion MenuItem - Category
  * PRIMERO SE DEBEN ELIMINAR LOS ITEMS RELACIONADOS CON LA CATEGORIA
  ? DESPUES SI ELIMINAR LA CATEGORIA ESPECIFICA
"""

# * MODELO DE ACTIVIDAD
# class Book(models.Model):
#   title = models.CharField(max_length = 255)
#   author = models.CharField(max_length = 255)
#   price = models.DecimalField(max_digits=5, decimal_places=2)
  
  # class Meta:
  #   indexes = [
  #     models.Index(fields=['price']),
  #   ]