from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100) # заголовок поста
    content = models.TextField() # содержание поста
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автор поста
    date_created = models.DateTimeField(auto_now_add=True) # дата создания поста

    def __str__(self):
        return self.title # возвращает заголовок поста при выводе на экран

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # пост, к которому относится комментарий
    name = models.CharField(max_length=50) # имя комментатора
    email = models.EmailField() # электронная почта комментатора
    content = models.TextField() # содержание комментария
    date_created = models.DateTimeField(auto_now_add=True) # дата создания комментария

    def __str__(self):
        return f"{self.name} on {self.post}" # возвращает имя комментатора и пост при выводе на экран
