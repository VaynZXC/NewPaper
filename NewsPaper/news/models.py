from django.db import models
from accounts.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_rating = models.IntegerField(default = 0)

class Category(models.Model):
    sport = 'SP'
    politics = 'PO'
    education = 'ED'
    leisure = 'LE'

    THEMES = [
          (sport, 'Спорт'),
          (politics, 'Политика'),
          (education, 'Образование'),
          (leisure, 'Досуг')
        ]
    
    category = models.CharField(max_length = 255, unique = True)
  
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    article_or_news = models.IntegerField(default = 1)
    time_in = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    title = models.CharField(max_length= 255)
    text = models.TextField(default = "Текст не указан")
    post_rating = models.IntegerField(default = 0)

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.TextField()
    time_in = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)