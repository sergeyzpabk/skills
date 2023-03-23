from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Urls, Urls_ebay
from django.views.generic.base import View

class UrlsView(View):
    def get(self, request):
        urls = Urls.objects.all()
        data = serializers.serialize('json', urls)
        return HttpResponse(data, content_type='application/json')

class UrlsEbayView(View):
    def get(self, request):
        urls = Urls_ebay.objects.all()
        data = serializers.serialize('json', urls)
        return HttpResponse(data, content_type='application/json')

