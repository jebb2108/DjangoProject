from django.shortcuts import render
from django.http import HttpResponse

about_me = {
'first_name': 'Габриэль',
'middle_name': 'Александр',
'last_name': 'Бушар',
'phone': '+7 (915) 079-1930',
'email': 'gabouchard2002@gmail.com',
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def index(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Бушар Габриэль</i>
    """
    return render(request, 'index.html')

def get_info(request):
    content = f""" <p>Имя: {about_me['first_name']}</p>
    <p>Второе имя: {about_me['middle_name']}</p> 
    <p>Фамилия {about_me['last_name']}</p>
    <p>Телефон: {about_me['phone']}</p>
    <p>Email: {about_me['email']}</p>"""
    return HttpResponse(content)


def get_item(request, item_number):
    obj = {}
    for item in items:
        if item['id'] == item_number:
            obj = item
    if obj:
        content = f"""
        <ul>
        <li>Id: {obj['id']}</li>
        <li>Name: {obj['name']}</li>
        <li>Quantity: {obj['quantity']}</li>
        </ul>
        """
        return HttpResponse(content)
    else:
        return HttpResponse('<p>Error</p>')




