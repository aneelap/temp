from django.contrib import admin
from .models import category

# Register your models here.

class Categoryslug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
    list_display_links = ('slug', 'category_name',)
admin.site.register(category,Categoryslug)
