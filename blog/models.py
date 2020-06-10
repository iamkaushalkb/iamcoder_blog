from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
# model for blog post  form 
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    author = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    slug = models.CharField(max_length = 255)
    content = models.TextField()
    timestamp = models.DateField(blank = True)
    
    def __str__(self):
        return 'Post From ' + self.author
    
# model for blog comment  form 
class BlogComment(models.Model):
   sno = models.AutoField(primary_key = True)
   comment = models.TextField(null = True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
   timestamp = models.DateField(default = now)
   
   def __str__(self):
         return 'Comment From ' + self.user.username
   