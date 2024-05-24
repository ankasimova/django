from django.http import HttpResponse

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
    return HttpResponse("Главная")

def about(request, name, age):

    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponse("Контакты")
