from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Product(models.Model):
    name=models.CharField(max_length=50,default=" ")
    price=models.DecimalField(decimal_places=2,max_digits=6)
    quanity=models.IntegerField(default=0)
    picture=models.ImageField(upload_to="product_images",blank=True)
    description=models.CharField(max_length=150,default=" ")
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(User)
    total_amount=models.DecimalField(decimal_places=2,max_digits=6)
    date_of_order=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return "%d %s".format(self.pk,self.customer.username)

class LineDetails(models.Model):
    order=models.ForeignKey(Order)
    product=models.ForeignKey(Product)
    quanity=models.IntegerField(default=1)
    price=models.DecimalField(decimal_places=2,max_digits=6)


class CartDetails(models.Model):
    cuser=models.ForeignKey(User)
    cproduct=models.ForeignKey(Product)
    quantity=models.IntegerField(default=1)

    @classmethod
    def deleteFromCart(cls,current_user,prod):
        cls.objects.filter(cuser=current_user,cproduct=prod).delete()

    def __str__(self):
        return str(self.cproduct.name)+"|"+str(self.cuser.username)
