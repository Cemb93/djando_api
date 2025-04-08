# from django.db import IntegrityError
# from django.http import HttpResponse, JsonResponse
# from .models import Book
# from django.views.decorators.csrf import csrf_exempt
# from django.forms.models import model_to_dict

# @csrf_exempt
# def books(request):
#   if request.method == 'GET':
#     books = Book.objects.all().values()
#     return JsonResponse({"books":list(books)})
#   elif request.method == 'POST':
#     title = request.POST.get('title')
#     author = request.POST.get('author')
#     price = request.POST.get('price')
#     book = Book(
#       title = title,
#       author = author,
#       price = price
#     )
#     try:
#       book.save()
#     except IntegrityError:
#       return JsonResponse({'error':'true','message':'required field missing'},status=400)

#     return JsonResponse(model_to_dict(book), status=201)

# * ==============================================================================

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Book, MenuItem
from rest_framework import generics
from .serializers import BookSerializer, MenuItemSerializer
from django.shortcuts import get_object_or_404

@api_view()
def menu_item(request):
  # items = MenuItem.objects.all()
  items = MenuItem.objects.select_related('category').all()
  serialized_item = MenuItemSerializer(items, many=True)
  return Response(serialized_item.data)

@api_view()
# ?       menu-items/<int:id>
def single_item(resquest, id):
  item = MenuItem.objects.select_related('category').get(pk=id)
  # item = get_object_or_404(MenuItem, pk=id)
  serialized_item = MenuItemSerializer(item)
  return Response(serialized_item.data)

class BookView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class MenuItemsView(generics.ListCreateAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer