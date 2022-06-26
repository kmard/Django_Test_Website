from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

# Register your models here.
"""
register crm ordrs
"""

#settings elements order
class Coment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_text','coment_dt')
    readonly_fields = ('coment_dt',)
    extra = 1


#setting up the fields of the orders admin window
class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_name', 'order_phone', 'order_status', 'order_dt')
    list_display_links = ('id', 'order_name',)
    search_fields = ('id', 'order_name', 'order_phone',)
    list_filter = ('order_phone', 'order_status')
    list_editable = ('order_phone', 'order_status')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('order_status','id', 'order_name', 'order_phone','order_dt')
    readonly_fields = ('id','order_dt')
    #field class comment
    inlines = [Coment,]



admin.site.register(Order,OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)