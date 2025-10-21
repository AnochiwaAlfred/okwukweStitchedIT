
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from products.models import Product
from orderitems.models import OrderItem
from accounts.models import MyUser
from django.http import HttpResponseForbidden
from django_countries import countries
from orders.models import Order
from orderhistory.models import OrderHistory
from django.contrib import messages
from paypal.standard.forms import PayPalPaymentsForm
import json
import uuid


# Create your views here.


def index(request):
    productList = Product.objects.all()
    pageName = 'Home'
    context = {
        'products':productList,
        'pageName':pageName,
    }
    message = request.GET.get('data')
    context.update({'message':message})
    return render(request, 'index.html', context)

@login_required()
def addToCart(request, id, productID):
    user = MyUser.objects.get(pk=id)
    product = Product.objects.get(productID=productID)
    itemList = OrderItem.objects.filter(product=product)
    cartList = user.cart.all()
    
    def checkItem():
        if itemList.count() != 0:
            item = OrderItem.objects.get(product=product)
            return item
        else:
            item = OrderItem(product=product, quantity=1)
            item.save()
            return item
    item = checkItem()
    
    print(cartList.count())
    
    if item in cartList:
        pass
    else:
        user.cart.add(item)
    user.save()
    for item in cartList:
        print(item)
    return redirect('/')

@login_required()
def removeFromCart(request, id, itemID):
    user = MyUser.objects.get(pk=id)
    item = OrderItem.objects.get(id=itemID)
    user.cart.remove(item)
    user.save()
    return cart(request, id)

@login_required()
def clearCart(request, id):
    user = MyUser.objects.get(pk=id)
    user.cart.clear()
    user.save()
    return redirect('/')

@login_required()
def cart(request, id):
    user = MyUser.objects.get(pk=id)
    if request.user != user:
        return HttpResponseForbidden()
    else:
        cartList = user.cart.all()
        context = {
            'cartList':cartList,
        }
        return render(request, 'cart.html', context)
        
def aboutView(request):
    pageName = 'About'
    context = {
        'pageName':pageName,
    }
    return render(request, 'about.html', context)

def contactView(request):
    pageName = 'Contact'
    context = {
        'pageName':pageName,
    }
    return render(request, 'contact.html', context)

@login_required()
def updateCart(request, id, item_id):
    user = MyUser.objects.get(id=id)
    if request.method=='POST':
        item = user.cart.get(id=item_id)
        quantity=json.loads(request.body)
        print('A -', quantity, item.quantity, item.product.quantityAvailable)
        if item.product.quantityAvailable>=quantity:
            item.quantity = quantity
            item.save()
        user.save()
        print('B -', quantity, item.quantity, item.product.quantityAvailable)
        print(f"Updated {user}'s cart")
    return render(request, 'cart.html')



@login_required()
def orderRequest(request, id):
    user = MyUser.objects.get(pk=id)
    cart = user.cart.all()
    total = sum([item.get_total for item in cart])
    COUNTRY = [name for (code, name) in countries]
    payments=[key for (key, value) in Order.PAYMENTMETHOD]
    
    host=request.get_host()
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "1000.00",
        "item_name": "Product 1",
        "invoice": str(uuid.uuid4()),
        'currenc_code': 'USD',
        "notify_url": f'http://{host}{reverse("paypal-ipn")}',
        "return_url": f'http://{host}{reverse("payment-done")}',
        "cancel_return": f'http://{host}{reverse("paypal-cancel")}',
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context={'total':total, 'countries':COUNTRY, 'payments':payments}
    context.update({"form": form, 'email':settings.PAYPAL_RECEIVER_EMAIL})
    return render(request, 'create-order.html', context)



@login_required()
def checkoutCart(request):
    if request.method=='POST':
        data = {
            'paymentMethod':request.POST.get('paymentMethod'), 
            'streetAddress':request.POST.get('streetAddress'), 
            'apartmentAddress':request.POST.get('apartmentAddress'),
            'state':request.POST.get('state'), 
            'city':request.POST.get('city'), 
            'country':request.POST.get('country'),
        }
        order = Order.objects.create(**data)
        user=request.user
        for item in user.cart.all():
            order.orderItems.add(item)
            item.reduce()
            item.save()
        order.save()
        if user.orderHistory==None:
            orderHistory=OrderHistory.objects.create()
            user.orderHistory=orderHistory
            user.save()
        user.orderHistory.orders.add(order)
        user.cart.clear()
        user.save()
    context={'message':'Purchase Successful'}
    # return render(request, 'index.html', context)
    return redirect('../../../?data=' + context['message'])





# # view_that_asks_for_money
# def home(request): 
#     host=request.get_host()
#     # What you want the button to do.
#     paypal_dict = {
#         "business": settings.PAYPAL_RECEIVER_EMAIL,
#         "amount": "1000.00",
#         "item_name": "Product 1",
#         "invoice": str(uuid.uuid4()),
#         'currenc_code': 'USD',
#         "notify_url": f'http://{host}{reverse("paypal-ipn")}',
#         "return_url": f'http://{host}{reverse("payment-done")}',
#         "cancel_return": f'http://{host}{reverse("paypal-cancel")}',
#     }

#     # Create the instance.
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context = {"form": form, 'email':settings.PAYPAL_RECEIVER_EMAIL}
#     return render(request, "about.html", context)


def payment_done(request):
    messages.success(request,' Youve successfully made a payment')
    return redirect('index')

def paypal_cancel(request):
    messages.error(request,' Youve successfully canceled a payment')
    return redirect('index')