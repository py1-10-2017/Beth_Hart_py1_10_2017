# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
        request.session['total'] = 0
        request.session['in_cart'] = 0
    return render(request, 'index.html')
    
def buy(request):
    price = 0
    qty = int(request.POST['qty'])
    item = request.POST['item']
    if item == 'shirt':
        price = 19.99
    elif item == 'sweater':
        price = 29.00
    elif item == 'cup':
        price = 4.99
    items = request.session['cart']
    new_item = {
        'item': request.POST['item'],
        'price' : price,
        'qty': request.POST['qty'],
    }
    for i in range(qty):
        items.append(new_item)
        request.session['total'] += price
    request.session['cart']= items
    request.session['in_cart'] = len(items)
    print(request.session['cart'])
    print (request.session['total'])
    return redirect('/')
    
def clear(request):
    #needs flash message and redirect
    del request.session['cart']
    return render(request, 'checkout.html')