from decimal import Decimal
from django.db import models
from django.db.models.signals import pre_save, post_save

from addresses.models import Address
from carts.models import Cart
from billing.models import BillingProfile
from eCommerce.utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):

        created = False
        #qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        #The same as code below
        qs = self.get_queryset().filter(billing_profile=billing_profile, cart=cart_obj, active=True, status='created')
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)
            created = True
        return obj, created


class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, blank=True, null=True, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120, blank=True)
    billing_address = models.ForeignKey(Address, related_name='billing_address', null=True, blank=True, on_delete=models.SET_NULL)
    shipping_address =  models.ForeignKey(Address, related_name='shipping_address', null=True, blank=True, on_delete=models.SET_NULL)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        order_total = Decimal(cart_total) + Decimal(shipping_total)
        self.total = round(order_total, 2)
        self.save()
        return order_total


    def check_done(self):
        if self.billing_profile and self.shipping_address and self.billing_address and self.total > 0:
            return True
        return False

    def mark_paid(self):
        if self.check_done():
            self.status = 'paid'
            self.save()
        return self.status

    objects = OrderManager()

#generate the order_id
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)

pre_save.connect(pre_save_create_order_id, sender=Order)

def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart_id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
       instance.update_total()

post_save.connect(post_save_order, sender=Order)