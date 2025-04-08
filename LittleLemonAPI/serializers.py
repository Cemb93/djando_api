from rest_framework import serializers
from .models import Book, MenuItem, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'slug', 'title']

# * SERIALIZANCION VIDEO
class MenuItemSerializer(serializers.ModelSerializer):
  stock = serializers.IntegerField(source='inventory')
  price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
  category = CategorySerializer(read_only=True)
  class Meta:
    model = MenuItem
    fields = ['id','title', 'price', 'stock', 'price_after_tax', 'category']
    extra_kwargs = {
      'price': {'min_value': 2},
      'inventory':{'min_value':0}
    }
  
  def calculate_tax(self, product: MenuItem):
    return product.price * Decimal(1.1)

# * SERIALIZACION ACTIVIDAD
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id','title','author','price']