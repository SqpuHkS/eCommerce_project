from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings

from .signals import analytic_signal
from .utils import get_client_ip

User = settings.AUTH_USER_MODEL

class Analytics(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) #User instance
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #User, Item, Order
    object_id = models.PositiveIntegerField() #user id, item id, order id
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content_object} viewed on {self.timestamp}'

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'

def analytic_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender) #instance.__class__
    user = request.user if request.user.is_authenticated else None
    new_analytic_obj = Analytics.objects.create(
        user=user,
        ip_address=get_client_ip(request),
        content_type=c_type,
        object_id=instance.id,
    )


analytic_signal.connect(analytic_receiver)