from django.db import models
from django.db.models import Sum
from shortuuid.django_fields import ShortUUIDField
from products.models import Product


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False, default='Ireland')
    postcode = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    county = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    delivery_cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _new_order_number(self):
        """
        Generate a new order number
        """
        return ShortUUIDField(
                            length=7,
                            max_length=10,
                            alphabet="abcdefg1234",
                            editable=False)

    def update_total(self):
        """
        Update order total and calculates shipping.  
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override original save method.
        """
        if not self.order_number:
            self.order_number = self._new_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    
    def save(self, *args, **kwargs):
        """
        override original save method
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)