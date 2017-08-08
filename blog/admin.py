# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    #fields display on change list
    list_display=['title','description']
    #fields to filter a changelsit with
    list_filter=['published','created']
    #fields to search in changelist
    search_fields=['title','description','content']
    #enable a date drill down
    date_hierarchy='created'
    #enable a save button on top of a change form
    save_on_top=True
    #prepopulate slug from title
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)
