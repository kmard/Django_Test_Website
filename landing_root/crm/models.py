from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Name of status')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200,verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='State')

    def __str__(self):
        # return self.order_name +' : '+ self.order_phone
        return self.order_name

    """
    single name for order
    plural name for order
    """
    class Meta:
        verbose_name        = 'Order'
        verbose_name_plural = 'Orders'

class ComentCrm(models.Model):
    coments_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    coment_text = models.TextField(verbose_name='Text comment')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Date create')

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

