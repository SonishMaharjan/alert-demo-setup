# from django.contrib import admin
# from . import models

# Register your models here.
# class AlertAdminArea(admin.AdminSite):
#     site_header = 'Alert Admin Are'
    
# alert_site = AlertAdminArea(name="AlertAdmin")

# alert_site.register(models.Post)
# admin.site.register(models.Post)

from django.contrib import admin
from .models import Post, Category

from django import forms


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    # ('author', 'slug' ) -> adds in same line q
    # fields = ['title', ('author', 'slug')]
    
    # Adding Section
    fieldsets = (
        ('The Sction 1', {'fields': ('title', 'author'), 'description': 'All fieds on this section are required'}),
        ('The Section 2', {'fields': ('slug',), 'classes':('collapse',)})
        )
    
    list_display = ('title', 'display_categories')

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# you can also use decorator
# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)

# Shows the models provided by Django in the Admin View.
from django.contrib import admin
import django.apps

models = django.apps.apps.get_models()


# this will register all your custom models too.
for model in models:
    try: 
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


admin.site.unregister(django.contrib.sessions.models.Session)
# admin.site.unregister(Post)


## create cusom form for admin

# class PostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['title'].help_text = 'New Help Text'

#     class Meta: 
#         model = Post
#         exclude = ('slug',)

# class PostFormAdmin(admin.ModelAdmin):
#     form = PostForm
    
# admin.site.register(Post, PostFormAdmin)