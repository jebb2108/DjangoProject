from .models import Item
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

about_me = {
    'first_name': 'Габриэль',
    'middle_name': 'Александр',
    'last_name': 'Бушар',
    'phone': '+7 (915) 079-1930',
    'email': 'gabouchard2002@gmail.com',
}


def index(request):
    content = {
        'name': "Бушар Габриэль Александр",
        'email': 'gabouchard2002@gmail.com',
    }
    return render(request, 'index.html', content)


def get_info(request):
    content = f""" <p>Имя: {about_me['first_name']}</p>
    <p>Второе имя: {about_me['middle_name']}</p> 
    <p>Фамилия {about_me['last_name']}</p>
    <p>Телефон: {about_me['phone']}</p>
    <p>Email: {about_me['email']}</p>"""
    return HttpResponse(content)


def get_item(request, item_number):
    item = get_object_or_404(Item, id=item_number)
    # item = next((item for item in items if item['id'] == item_number), None)
    content = {
        'item': item,
    }
    
    return render(request, 'item.html', content)


def get_all_items(request):
    items = Item.objects.all()
    content = {
        'items': items
    }
    return render(request, 'items.html', content)