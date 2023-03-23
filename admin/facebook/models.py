from django.db import models

# Create your models here.

class Urls(models.Model):
    url = models.CharField('Ссылка', max_length=250)
    def __str__(self):
        return f'{self.url}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

class Urls_ebay(models.Model):
    url = models.CharField('Urls Ebay', max_length=250)
    proxy = models.CharField('Proxy', max_length=250)
    nameProfile = models.CharField('Name Profile', max_length=250, unique=True)
    def __str__(self):
        return f'{self.url}'

    class Meta:
        verbose_name = 'Urls Ebay'
        verbose_name_plural = 'Urls Ebay'
