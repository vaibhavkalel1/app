from django.shortcuts import render, redirect
from .models import Pencil

def pencil_list(request):
    pencils = Pencil.objects.all()
    return render(request, 'marketplace/pencil_list.html', {'pencils': pencils})

def sell_pencil(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        seller = request.POST.get('seller')
        Pencil.objects.create(name=name, price=price, seller=seller)
        return redirect('pencil_list')
    return render(request, 'marketplace/sell_pencil.html')
