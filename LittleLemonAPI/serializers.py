from rest_framework import serializers
from .models import Book, MenuItem

# * SERIALIZANCION VIDEO
class MenuItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = MenuItem
    fields = ['id','title', 'price', 'inventory']
    extra_kwargs = {
      'price': {'min_value': 2},
      'inventory':{'min_value':0}
    }

# * SERIALIZACION ACTIVIDAD
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id','title','author','price']