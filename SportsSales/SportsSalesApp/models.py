from django.db import models
from django.contrib.auth.models import User

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Order
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length = 30)

    # Clear Database Visibility
    def __str__(self):
        return f'Order No.{self.order_id} - {self.user} - Status {self.status}'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Item
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Item(models.Model):
    item_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)
    price = models.FloatField()
    description = models.CharField(max_length = 30)

    # Clear Database Visibility
    def __str__(self):
        return f'{self.name}'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Order Item
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OrderItem(models.Model):
    orderItem_id = models.IntegerField(primary_key = True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField()

    # Clear Database Visibility
    def __str__(self):
        return f'Order No. {self.orderItem_id} - {self.item} - (x{self.quantity})'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Role
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Role(models.Model):
    role_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)

    # Clear Database Visibility
    def __str__(self):
        return f'Role No.{self.role_id} - {self.name}'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Payment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Payment(models.Model):
    payment_id = models.IntegerField(primary_key = True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    type = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)

    # Clear Database Visibility
    def __str__(self):
        return f'Payment No.{self.payment_id} - VIA {self.type} - Status: {self.status}'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extension To User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)