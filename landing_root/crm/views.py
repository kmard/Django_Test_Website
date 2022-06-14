from django.shortcuts import render
from .models import Order  # imoprt class order
from .forms import OrderForm #import class OrderForm

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request,'./index.html',{'object_list':object_list,
                                          'form':form})

#Page after sending registration
def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    # write contact data to mysql
    element = Order(order_name=name,order_phone=phone)
    element.save()

    return render(request,'./thanks_page.html',{'name':name,'phone':phone})
