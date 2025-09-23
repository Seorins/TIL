from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # auto_now_add = 최초 작성일만 기록
    create_at = models.DateTimeField(auto_now_add=True)
    # auto_now = 수정할 때마다 기록
    updated_at = models.DateTimeField(auto_now=True)