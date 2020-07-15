from django.db import models
from django.conf import settings
from items.models import Item
from django.db.models.signals import pre_save, post_save, m2m_changed

# Create your models here.
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):

    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
            # cart_id exists
        else:
            cart_obj = Cart.objects.new_cart(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj


    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    items = models.ManyToManyField(Item, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

# many to many signal
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        items = instance.items.all()
        total = 0
        for i in items:
            total += i.price
        # For reason to not repeat and call the save method without any changes
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.items.through)

def cart_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal 

pre_save.connect(cart_pre_save_receiver, sender=Cart)


