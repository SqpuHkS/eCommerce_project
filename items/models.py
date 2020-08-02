import os
import random
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from eCommerce.utils import unique_slug_generator
from django.urls import reverse

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 41209484)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'items/{new_filename}/{final_filename}'



class ItemManager(models.Manager):
    def search(self, query):
        lookups = ( Q(title__icontains=query) |
                    Q(description__icontains=query) |
                    Q(price__icontains=query) |
                    Q(tag__title__icontains=query)
                    )
        return Item.objects.filter(lookups).distinct()

class Item(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('items:detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title + '/'+ self.slug

    objects = models.Manager()
    active_objects = ItemManager()


def item_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(item_pre_save_receiver, sender=Item)