from django.urls import path
from . import views

urlpatterns = [
    #son vistas de ejemplo
    path('', views.login, name='login'),  # Ruta para la vista login
    path('register/', views.register, name='register'),  # Ruta para la vista login
    path('profile/', views.profile, name='profile'),  # Ruta para la vista login
    path('index/', views.index, name='index'),  # Ruta para la vista index
    path('about/', views.about, name='about'),# Ruta para la vista about
    path('contact/', views.contact, name='contact'),# Ruta para la vista contact
    path('home/', views.home, name='home'),# Ruta para la vista home
    path('principios/', views.principios, name='principios'),# Ruta para la vista principios
    path('preguntasAccesibilidad/', views.preguntasAccesibilidad, name='preguntasAccesibilidad'),# Ruta para la vista preguntas
    path('preguntasCentradoUsuario/', views.preguntasCentradoUsuario, name='preguntasCentradoUsuario'),# Ruta para la vista preguntas
    path('preguntasConsistencia/', views.preguntasConsistencia, name='preguntasConsistencia'),# Ruta para la vista preguntas
    path('preguntasSimplicidad/', views.preguntasSimplicidad, name='preguntasSimplicidad'),# Ruta para la vista preguntas
    path('preguntasUsabilidad/', views.preguntasUsabilidad, name='preguntasUsabilidad'),# Ruta para la vista preguntas
    # Aquí puedes añadir más rutas para otras vistas de rubrica
]
 