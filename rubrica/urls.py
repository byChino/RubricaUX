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
    # Aquí puedes añadir más rutas para otras vistas de rubrica
]
