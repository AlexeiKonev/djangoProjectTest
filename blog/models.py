from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100) # заголовок поста
    content = models.TextField() # содержание поста
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автор поста
    date_created = models.DateTimeField(auto_now_add=True) # дата создания поста

    def __str__(self):
        return self.title # возвращает заголовок поста при выводе на экран
