from django.shortcuts import render
from .models import Order  # imoprt class order

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    return render(request,'./index.html',{'object_list':object_list})