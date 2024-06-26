from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render
from .forms import UserForm


# def index(request):
#     host = request.META["HTTP_HOST"]
#     user_agent = request.META["HTTP_USER_AGENT"]
#     path = request.path
#
#     return HttpResponse(f"""
#         <p>Host: {host}</p>
#         <p>User-Agent: {user_agent}</p>
#         <p>Path: {path}</p>
#     """)

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


# def contact(request):
#     return HttpResponse("Контакты")

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


#Установка куки
# def set(request):
#     username = request.GET.get("username", "Undefined")
#     response = HttpResponse(f'Hello {username}')
#     response.set_cookie("username", username, httponly=True, secure=True)
#     return response


#Получение куки
# def get(request):
#     username = request.COOKIES['username']
#     return HttpResponse(f'Hello {username}')


#Рендер с помощью templates, передача данных в шаблоны в виде переменных


#def index(request):
    #header = "Информация о пользователе"     # простой текст
    #langs = ["en", "ru", "kk"]               # список
    #user = {"name": "Lika", "age": "27"}     # словарь
    #address = ("Auezov", 212, 132)           # кортеж
    #data = {"header": header, "langs": langs, "user": user, "address": address}
    #return render(request, "index.html", context=data)


def static(request, ):
    return render(request, "static.html")

def base(request):
    return render(request, "base.html")

def ind(request):
    return render(request, "ind.html")

def contact(request):
    return render(request, "contact.html")

def userform(request):
    return render(request, "userform.html")

def postuser(request):
    name = request.POST.get("name", "Undefined")
    date_of_birth = request.POST.get("date of birth", 0)
    age = request.POST.get("age", 0)
    status = request.POST.get("married")
    phone_number = request.POST.get("phone number", 0)
    email = request.POST.get("email", 0)
    languages = request.POST.getlist("languages", ["python"])
    return HttpResponse(f'<h2>Имя: {name} Возраст: {age} Дата рождения: {date_of_birth} ЯП: {languages}</h2>')

# def userforms(request):
#     userforms = UserForms()
#     return render(request, "userindex.html", {"form": userforms})

def userindex(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse(f"<h2>Hello, {name}</h2>")
    return render(request, "userindex.html", {"form": userform})

