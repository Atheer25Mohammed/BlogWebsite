from django.db import models
from datetime import datetime    

# Create your models here.
class User(models.Model):
     user_id = models.CharField(max_length=30)
     Username = models.CharField(max_length=30)
     Email = models.CharField(max_length=30)
     Password = models.CharField(max_length=30)
    
class Post(models.Model):
     post_id = models.CharField(max_length=50)
     Title = models.CharField(max_length=50)
     Content = models.CharField(max_length=100)
     Category = models.CharField(max_length=100)
     Date = models.DateTimeField(default=datetime.now, blank=True)

class Comment(models.Model):
     comment_id = models.CharField(max_length=50)
     Post_ID = models.ForeignKey(Post, on_delete=models.CASCADE)
     User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
     Content = models.CharField(max_length=100)
     Date = models.DateTimeField(default=datetime.now, blank=True)
    
class Category(models.Model):
     cat_id = models.CharField(max_length=50)
     Name = models.CharField(max_length=100)