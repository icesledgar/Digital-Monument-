from django.contrib import admin
from .models import Monument

class MonumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_built', 'image')

admin.site.register(Monument, MonumentAdmin)