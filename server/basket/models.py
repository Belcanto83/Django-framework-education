from django.db import models

# Create your models here.


class Orders(models.Model):
    user = models.ForeignKey(
        'accounts.AccountUser',
        on_delete=models.DO_NOTHING,
    )
    order_date_time = models.DateTimeField(
        auto_now=True,
    )
    order_is_finished = models.BooleanField(
        default=False
    )


class OrderedProducts(models.Model):
    class Meta:
        unique_together = (('order', 'product'),)

    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    ordered_products_qty = models.PositiveSmallIntegerField(
        default=1
    )
