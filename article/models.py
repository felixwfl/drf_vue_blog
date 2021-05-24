from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdown import Markdown


# Create your models here.
class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')


class Tag(models.Model):
    """文章标签"""
    text = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class Category(models.Model):
    """文章分类"""
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100)

    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    # 作者 一个作者可以有多个文章
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    # 分类 一个类别可以有多个文章
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )
    # 标签 一个标签可以有多个文章 反之亦然
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles'
    )
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )

    # 新增方法，将 body 转换为带 html 标签的正文
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        # toc 是渲染后的目录
        return md_body, md.toc

    class Meta:
        ordering = ['-created']  # 按照创建的时间逆排序

    def __str__(self):
        return self.title
