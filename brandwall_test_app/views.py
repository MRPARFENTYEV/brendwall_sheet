from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer


class ProductList(APIView):
    # Получение списка всех продуктов
    # def get(self, request):
    #     if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Проверяем, является ли запрос AJAX-запросом
    #         products = Product.objects.all()
    #         serializer = ProductSerializer(products, many=True)
    #         print(products)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         # Возвращаем HTML-страницу при обычном запросе
    #         return render(request, 'products.html')
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        if len(products) < 1:
            return Response('Пока нет ни одного продукта')
        else:
            # return Response(serializer.data, status=status.HTTP_200_OK)
            return render(request, 'products.html')

    # Создание нового продукта
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductData(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
