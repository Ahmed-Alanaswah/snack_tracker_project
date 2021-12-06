from django.contrib import admin
from .models import Snacks
# Register your models here.


@admin.register(Snacks)
class AdminClass(admin.ModelAdmin):
    list_display=['name','purchaser']
    search_fields = ['name']
    list_display_links =('purchaser',)
# admin.site.register(Snacks) 