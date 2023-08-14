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


for model in models:
    try: 
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


admin.site.unregister(django.contrib.sessions.models.Session)

