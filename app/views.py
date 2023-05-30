
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from products.models import Product
from orderitems.models import OrderItem
from accounts.models import MyUser
from django.http import HttpResponseForbidden


# Create your views here.


def index(request):
    productList = Product.objects.all()
    pageName = 'Home'
    context = {
        'products':productList,
        'pageName':pageName,
    }
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
def removeFromCart(request, id, productID):
    user = MyUser.objects.get(pk=id)
    product = Product.objects.get(productID=productID)
    user.cart.remove(product)
    user.save()
    cartList = user.cart.all()
    for item in cartList:
        print(item)
    return redirect('/')

@login_required()
def clearCart(request, id, productID):
    user = MyUser.objects.get(pk=id)
    user.cart.clear()
    user.save()
    cartList = user.cart.all()
    for item in cartList:
        print(item)
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
