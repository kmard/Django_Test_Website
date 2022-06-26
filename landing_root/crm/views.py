from django.shortcuts import render
from .models import Order  # imoprt class order
from .forms import OrderForm #import class OrderForm
from cms.models import  CmsSlider
from price.models import PriceCard,PriceTable
from telebot.sendmessage import sendTelegram


# Create your views here.
def first_page(request):
    # object_list = Order.objects.all()
    # form = OrderForm()
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list':slider_list,
                'pc_1':pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table':price_table,
                'form' : form,
                }
    return render(request,'./index.html',dict_obj)


#Page after sending registration
def thanks_page(request):
    if request.POST :
        name = request.POST['name']
        phone = request.POST['phone']
        # write contact data to mysql
        element = Order(order_name=name,order_phone=phone)
        element.save()
        sendTelegram(name, phone)
        return render(request,'./thanks_page.html',{'name':name,'phone':phone})
    else:
        return render(request, './thanks_page.html')
