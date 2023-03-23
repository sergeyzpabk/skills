from django.contrib import admin

from .models import Urls, Urls_ebay
# Register your models here.

@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('url',)

@admin.register(Urls_ebay)
class UrlsEbayAdmin(admin.ModelAdmin):
    list_display = ('url','proxy', 'nameProfile')

