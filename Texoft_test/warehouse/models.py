from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy
from simple_history.models import HistoricalRecords


class Product(models.Model):

    title = models.CharField('Name product', max_length=50, unique=True)
    description = models.TextField(verbose_name='Description product', max_length=500, blank=True)
    price = models.DecimalField(verbose_name='Price product', max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0)], default=0)
    count = models.PositiveIntegerField(verbose_name='Count product', default=0)
    category = models.ForeignKey('Category', verbose_name='Category', on_delete=models.PROTECT)

    history = HistoricalRecords(excluded_fields=['category', 'price', 'description'],)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['title']


class Category(models.Model):

    title = models.CharField(verbose_name='Name category', max_length=30, unique=True)
    description = models.TextField(verbose_name='Description category', max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
