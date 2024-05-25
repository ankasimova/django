from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>User-Agent: {user_agent}</p>
        <p>Path: {path}</p>
    """)

def main(request):
    return HttpResponse("Главная", status=400, reason="Incorrect Request")

def user(request, name='Не введено', age=0):

    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

#передача через query params в формате http://127.0.0.1:8000/aboutuser/?name=Lika&age=27
def aboutuser(request):
    name = request.GET.get('name', 'Не передано')
    age = request.GET.get('age', 0)
    return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")


def contact(request):
    return HttpResponse("Контакты")

def products(request, id):
    return HttpResponse(f"Продукт {id}")

def top(request):
    return HttpResponse("Топ товаров")

def new(request):
    return HttpResponse("Новые товары")

def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")

def questions(request, id):
    return HttpResponse(f'Вопросы о товаре {id}')


#Обработка кодов ошибок
def index(request, id):
    people = ["Данияр", "Диас", "Даулет"]
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Пользователь не найден")

def age(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Возраст указан некорректно")
    elif age < 18:
        return HttpResponseForbidden("Лицам до 18 лет доступ запрещен")
    else:
        return HttpResponse(f"Доступ разрешен. Возраст: {age}")