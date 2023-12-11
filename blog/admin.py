from django.contrib import admin
from . import models

# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'

blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(models.User)
blog_site.register(models.Post)
blog_site.register(models.Comment)
blog_site.register(models.Category)

