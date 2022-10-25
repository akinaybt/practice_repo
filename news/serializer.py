from rest_framework import serializers
from .models import News, Category


class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',)


class NewsDetailsSerializer(serializers.ModelSerializer):
    category_title = serializers.SerializerMethodField()

    def get_category_title(self, obj):
        return obj.category.title

    class Meta:
        model = News
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


