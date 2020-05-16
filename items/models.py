from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

class Item(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image = models.ImageField(upload_to='items/', null=True, blank=True)

def item_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(item_pre_save_receiver, sender=Item)
