from .serializer import (
    NewsListSerializer,
    NewsDetailsSerializer,
    NewsDeleteSerializer,
    NewsUpdateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryUpdateSerializer,
    CategoryDeleteSerializer
)
from .models import Category, News
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


class NewsDestroyAPIView(DestroyAPIView):
    serializer_class = NewsDeleteSerializer
    queryset = News.objects.all()
    lookup_field = 'title'


class NewsRetrieveAPIView(RetrieveAPIView):
    serializer_class = NewsDetailsSerializer
    queryset = News.objects.all()


class NewsListAPIView(ListCreateAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()


class NewsUpdateAPIView(UpdateAPIView):
    serializer_class = NewsUpdateSerializer
    queryset = News.objects.all()


class CategoryListAPIView(ListCreateAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryDeleteAPIView(DestroyAPIView):
    serializer_class = CategoryDeleteSerializer
    queryset = Category.objects.all()
    lookup_field = 'title'


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategoryUpdateSerializer
    queryset = Category.objects.all()
    lookup_field = 'title'


class CategoryDetailAPIView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    lookup_field = 'title'



