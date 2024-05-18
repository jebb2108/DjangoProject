from django.shortcuts import render
from django.http import HttpResponse

first_name = 'Габриэль'
middle_name = 'Александр'
last_name = 'Бушар'
phone = '+7 (915) 079-1930'
email = 'gabouchard2002@gmail.com'

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
    return HttpResponse(text)

def get_info(request):
    global first_name, middle_name, last_name, phone, email
    content = f""" <p>Имя: {first_name}</p>
    <p>Второе имя: {middle_name}</p> 
    <p>Фамилия {last_name}</p>
    <p>Телефон: {phone}</p>
    <p>Email: {email}</p>"""
    return HttpResponse(content)




