from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    uid = models.UUIDField('テストID',default=uuid.uuid4, editable=False)
    title = models.CharField('タイトル', max_length=100)
    category = models.CharField('カテゴリー', max_length=10)
    author = models.CharField('著者', max_length=20)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    update_at = models.DateTimeField('更新日', auto_now=True)
