from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Item

# Register your models here.
admin.site.register(Item, ItemAdmin)