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
  
  path('categories', views.CategoriesView.as_view()),
  path('categories/<int:pk>', views.SingleCategoryView.as_view()),
  path('menu-items', views.MenuItemsViewSet.as_view()),
  path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
  # path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
  # path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view()),
]