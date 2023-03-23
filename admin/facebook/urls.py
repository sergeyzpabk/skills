from django.urls import path
from . import  views

urlpatterns = [
    path('fc', views.UrlsView.as_view()),
    path('ebay', views.UrlsEbayView.as_view())
    ]

