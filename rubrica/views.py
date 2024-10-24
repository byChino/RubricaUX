from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def principios(request):
    return render(request, 'principios.html')

def preguntasAccesibilidad(request):
    return render(request, 'preguntasAccesibilidad.html')

def preguntasCentradoUsuario(request):
    return render(request, 'preguntasCentradoUsuario.html')

def preguntasConsistencia(request):
    return render(request, 'preguntasConsistencia.html')

def preguntasSimplicidad(request):
    return render(request, 'preguntasSimplicidad.html')

def preguntasUsabilidad(request):
    return render(request, 'preguntasUsabilidad.html')