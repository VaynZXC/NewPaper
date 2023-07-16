from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max

class Test(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)

class Author(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_rating = models.IntegerField(default = 0)

    def like(self):
      self.user_rating += 1

    def dislike(self):
      self.user_rating -+ 1

    def rating_clear(self):
      self.user_rating = 0

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
    
    category = models.CharField(max_length = 255)
  
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    article = 'AR'
    news = 'NE'

    TYPE = [
        (article, 'Статья'),
        (news, 'Новость')
        ]

    art_or_news = models.CharField(max_length= 20, default = article)
    time_in = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    title = models.CharField(max_length= 255)
    text = models.TextField(default = "Текст не указан")
    post_rating = models.IntegerField(default = 0)

    def like(self):
      self.post_rating += 1

    def dislike(self):
      self.post_rating -+ 1

    def rating_clear(self):
      self.post_rating = 0

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.TextField()
    time_in = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)

    def like(self):
      self.comment_rating += 1

    def dislike(self):
      self.comment_rating -+ 1

    def rating_clear(self):
      self.comment_rating = 0

def bestUser():
    best_user = User.objects.all()
    best_user.aggregate(Max('user_rating'))
    print(best_user)