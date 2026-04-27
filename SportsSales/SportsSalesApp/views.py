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

        user = request.user

        new_order = Order.objects.filter(user=request.user, status="Pending").first()

        if not new_order:
            new_order = Order.objects.create(
                user=request.user,
                status="Pending",
                date=datetime.date.today()
            )

        if item_id:
            item = Item.objects.get(pk = item_id)

            existing = OrderItem.objects.filter(order = new_order, item = item).first()

            if existing:
                existing.quantity += 1
                existing.save()
            else:
                OrderItem.objects.create(
                    order = new_order,
                    item = item,
                    quantity = 1
                )

    profile = getattr(request.user, 'userprofile', None)

    if not profile:
        # create one automatically
        profile = UserProfile.objects.create(user=request.user)

    role = profile.role.name if profile.role else "Customer"
    role = profile.role.name

    if role in ["Admin", "Manager"]:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)

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

def checkout(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")

        if not order_id:
            return redirect("order")

        order = Order.objects.get(order_id=order_id)

        order.status = "Completed"
        order.save()

        return redirect("/order/")