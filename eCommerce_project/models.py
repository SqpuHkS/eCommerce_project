from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image = models.ImageField(upload_to='items/', null=True, blank=True)

