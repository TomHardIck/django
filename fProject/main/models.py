from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    storage1 = models.PositiveIntegerField(default=0)
    storage2 = models.PositiveIntegerField(default=0)
    unallocated = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail',
                       args=[self.id, self.slug])