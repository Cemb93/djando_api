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

@api_view(['GET', 'POST'])
def menu_item(request):
  if request.method == 'GET':
    items = MenuItem.objects.select_related('category').all()
    # * FILTROS Y BUSQUEDA
    category_name = request.query_params.get('category')
    price = request.query_params.get('price')
    search = request.query_params.get('search')
    if category_name:
      # ! AGREGAR DOS GIONES "__" ENTRE EL MODELO Y EL CAMPO EN RELACION, EN ESTE CASO "title"
      items = items.filter(category__title=category_name)
    if price:
      items = items.filter(price__lte=price)
    if search:
      # ! AGREGAR DOS GIONES "__"
      items = items.filter(title__istartswith=search)
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)
  if request.method == 'POST':
    serialized_item = MenuItemSerializer(data=request.data)
    serialized_item.is_valid(raise_exception=True)
    serialized_item.save()
    return Response(serialized_item.data, status.HTTP_201_CREATED)

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