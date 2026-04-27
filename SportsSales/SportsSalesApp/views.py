from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
import datetime

def items(request):
    items = Item.objects.all()
    return render(request, 'item.html', {'items': items})

def order(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')

        user = User.objects.get(id=1)

        new_order = Order.objects.last()

        item = Item.objects.get(item_id=item_id)

        existing = OrderItem.objects.filter(order=new_order, item=item).first()

        if existing:
            existing.quantity += 1
            existing.save()
        else:
            OrderItem.objects.create(
                order=new_order,
                item=item,
                quantity=1
            )

    orders = Order.objects.all()
    return render(request, 'order.html', {'orders': orders})

def home(request):
    return HttpResponse('Home Page')

@login_required
def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'all_orders.html', {'orders': orders})

@login_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        order.status = new_status
        order.save()
        return redirect('all_orders')

    return render(request, 'update_order.html', {'order': order})