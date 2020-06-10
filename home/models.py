from django.db import models

# Create your models here.
# model for contact form 
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    msg = models.TextField()
    timestamp = models.TimeField(auto_now_add = True, blank = False)
    
    def __str__(self):
        return 'Message From ' + self.name
    