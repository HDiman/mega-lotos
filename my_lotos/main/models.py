from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here
class Category(MPTTModel):
    title = models.CharField(max_length=250, verbose_name='Название категории')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, db_index=True, related_name='children', verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['title']


class Grid(models.Model):
    item_0 = models.CharField('Item_0', max_length=100)
    item_1 = models.CharField('Item_1', max_length=100)
    item_2 = models.CharField('Item_2', max_length=100)
    item_3 = models.CharField('Item_3', max_length=100)
    item_4 = models.CharField('Item_4', max_length=100)
    item_5 = models.CharField('Item_5', max_length=100)
    item_6 = models.CharField('Item_6', max_length=100)
    item_7 = models.CharField('Item_7', max_length=100)
    item_8 = models.CharField('Item_8', max_length=100)

    def __str__(self):
        return self.item_0

