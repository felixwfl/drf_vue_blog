from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser  # 权限
from rest_framework import viewsets, filters
from article.permissions import IsAdminUserOrReadOnly  # 权限

from django.http import Http404

from article.models import Article, Category, Tag, Avatar

# from article.serializers import ArticleDetailSerializer, ArticleListSerializer
from article.serializers import ArticleSerializer, CategorySerializer, CategoryDetailSerializer, TagSerializer, \
    ArticleDetailSerializer, AvatarSerializer


# class ArticleList(generics.ListCreateAPIView):
#     # queryset和serializer_class是固定的写法
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]  # 用户权限 list中可以设置多个
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)  # 自适应添加文章作者
#
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)  # 自适应添加文章作者


class ArticleViewSet(viewsets.ModelViewSet):
    """博文视图集"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return SomeSerializer
    #     else:
    #         return AnotherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None  # 不翻页

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    """标签视图集"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None  # 不翻页


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]

