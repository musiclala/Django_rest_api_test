from django.urls import path
from .views import *

urlpatterns = [
    path('api/', ProductListView.as_view()),
    path('api/product/<int:pk>', ProductDetailView.as_view()),
    path('api/product/create/', CreateProductView.as_view()),
    path('api/product/update/<int:pk>', UpdateProductView.as_view()),
    path('api/product/delete/<int:pk>', DeleteProductView.as_view()),

    path('api/category/', CategoryListView.as_view()),
    path('api/category/create/', CreateCategoryView.as_view()),
    path('api/category/update/<int:pk>', UpdateCategoryView.as_view()),
    path('api/category/delete/<int:pk>', DeleteCategoryView.as_view()),


]