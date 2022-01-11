from rest_framework import generics, permissions


from .models import Product, Category
from .serializers import \
    ProductListSerializer, \
    ProductDetailSerializer, \
    CategoryListSerializer, \
    CRUDProductSerializer, \
    CRUDCategorySerializer
from .service import PaginationProduct


class ProductListView(generics.ListAPIView):
    """List product"""
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = PaginationProduct


class ProductDetailView(generics.RetrieveAPIView):
    """Detail product"""
    queryset = Product.objects.filter()
    serializer_class = ProductDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CategoryListView(generics.ListAPIView):
    """List category"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateCategoryView(generics.CreateAPIView):
    """Create category"""
    queryset = Category.objects.all()
    serializer_class = CRUDCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class UpdateCategoryView(generics.RetrieveUpdateAPIView):
    """Update category"""
    queryset = Category.objects.all()
    serializer_class = CRUDCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class DeleteCategoryView(generics.DestroyAPIView):
    """Delete category"""
    queryset = Category.objects.all()
    serializer_class = CRUDCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateProductView(generics.CreateAPIView):
    """Create category"""
    queryset = Product.objects.all()
    serializer_class = CRUDProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UpdateProductView(generics.RetrieveUpdateAPIView):
    """Update category"""
    queryset = Product.objects.all()
    serializer_class = CRUDProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DeleteProductView(generics.DestroyAPIView):
    """Delete category"""
    queryset = Product.objects.all()
    serializer_class = CRUDProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
