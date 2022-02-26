from django.contrib import admin
from .models import Base


@admin.register(Base)
class PostAdmin(admin.ModelAdmin):
    list_display = ('phone_models', 'imei', 'organization',)