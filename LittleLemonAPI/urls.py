from django.urls import path
from . import views

urlpatterns = [
  # path('books',views.books),
  # path('books', views.BookView.as_view()),
  # path('books/<int:pk>', views.SingleBookView.as_view()),
  # path('menu-items', views.MenuItemsView.as_view()),
  # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
  
  # path('menu-items', views.menu_item),
  # path('menu-items/<int:id>', views.single_item),
  
  path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
  path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
]