from django.shortcuts import render

from store.models import Customer, Product
from .models import *

def store(request):
	products = Product.objects.all()
	context = {'products' :products}
	return render(request, 'store/store.html', context)

def login(request):
	 return render(request,'store/login.html')


def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order={'get_cart_total':0,'get_cart_items':0}

	context = {'items':items,'order':order}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		order,created=Order.objects.get_or_create(customer=customer,complete=False)
		items=order.orderitem_set.all()
	else:
		order={'get_cart_total':0,'get_cart_items':0}
		items = []
	context = {'items':items,'order':order}
	return render(request, 'store/checkout.html', context)