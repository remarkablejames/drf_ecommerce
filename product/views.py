from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category, Product, Brand
from .serializers import CategorySerializer


# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    """ A simple ViewSet for viewing Categories."""
    queryset = Category.objects.all()

    @extend_schema(responses={200: CategorySerializer})
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
