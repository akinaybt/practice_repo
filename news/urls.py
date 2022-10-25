from django.urls import path
from . import views
urlpatterns = [
    path('news-list/', views.NewsListAPIView.as_view()),
    path('news-detail/<int:pk>/', views.NewsRetrieveAPIView.as_view()),
    path('news-delete/<str:title>/', views.NewsDestroyAPIView.as_view()),
    path('news-update/<int:pk>/', views.NewsUpdateAPIView.as_view()),
    path('category-list/', views.CategoryListAPIView.as_view()),
    path('category-update/<str:title>/', views.CategoryUpdateAPIView.as_view()),
    path('category-detail/<str:title>/', views.CategoryDetailAPIView.as_view()),
    path('category-delete/<str:title>/', views.CategoryDeleteAPIView.as_view()),
]

