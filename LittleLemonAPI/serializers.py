from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'title']
    # fields = ['id', 'slug', 'title']

# * SERIALIZANCION VIDEO
class MenuItemSerializer(serializers.ModelSerializer):
  stock = serializers.IntegerField(source='inventory')
  price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
  category = CategorySerializer(read_only=True)
  category_id = serializers.IntegerField(write_only=True)# ? SE USA PARA EL POST EN LA RELACION
  class Meta:
    model = MenuItem
    fields = ['id','title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
    # extra_kwargs = {
    #   'price': {'min_value': 2},
    #   'inventory':{'min_value':0}
    # }
  
  def validate(self, attrs):
    if attrs['price'] < 2:
      raise serializers.ValidationError('Price should not be less than 2.0')
    if attrs['inventory'] < 0:
      raise serializers.ValidationError('Stock cannot be negative')
    return super().validate(attrs)
  
  def calculate_tax(self, product: MenuItem):
    return product.price * Decimal(1.1)

# * SERIALIZACION ACTIVIDAD
# class BookSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Book
#     fields = ['id','title','author','price']