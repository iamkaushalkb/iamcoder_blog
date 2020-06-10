from django.contrib import admin
from blog.models import Post, BlogComment

# registering model
admin.site.register((Post, BlogComment))