# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique='true',max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default='true')
    created = models.DateTimeField(auto_now_add='true')
    
    class Meta:
        ordering=['-created']
    
    def _unicode_(self):
        return u'%s'%self.title
      
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
    
class Comment(models.Model):
    slug = models.ForeignKey(Post, on_delete = models.CASCADE, editable=False )
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    
    
   
    