"""
URL configuration for trabajo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  # Importa el módulo de administración de Django.
from django.urls import path  # Importa la función 'path' del módulo 'urls' de Django, que se utiliza para definir las rutas URL de la aplicación.
from contactos import views  # Importa las vistas definidas en el módulo 'views' de la aplicación 'contactos'. Estas vistas manejan las solicitudes HTTP para la aplicación.
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django, como LoginView, LogoutView, PasswordResetView, etc., y las asigna a un alias 'auth_views' para evitar conflictos de nombres.

urlpatterns = [
    # Rutas principales
    path('', views.home, name='home'), # Pagina de inicio.
    path('signup/', views.signup, name='signup'), # Registro de usuario
    path('signin/', views.signin, name='signin'), # Inicio de sesión
    path('logout/', views.sign_off, name='logout'),  # Cierre de sesión
    path('accounts/login/', auth_views.LoginView.as_view(template_name='mensaje.html'), name='mensaje'),  # Vista de aviso de inicio de sesión en caso de no estar registrado.

    # Rutas relacionadas con la gestión de contactos
    path('verinsert/', views.form_insert, name='verinsert'),  # Vista para mostrar formulario de inserción
    path('formActualizar/<id>', views.form_update, name='formActualizar'),  # Vista para mostrar formulario de actualización de contacto
    path('formNota/<id>', views.form_note, name='formNota'),  # Vista para mostrar formulario de inserción de nota para un contacto

    # Rutas para operaciones CRUD de contactos.
    path('select/', views.select, name='select'), # Vista para seleccionar y mostrar contactos
    path('insert/', views.insert, name='insert'),  # Vista para insertar un nuevo contacto
    path('update', views.update, name='update'),  # Vista para actualizar un contacto existente
    path('delete/<id>', views.delete, name='delete'), # Vista para eliminar un contacto

    # Rutas relacionadas con la gestión de notas.
    path('insertNote/', views.insert_note, name='insertNote'), # Vista para insertar una nueva nota para un contacto
    path('nota/', views.note, name='nota'), # Vista para mostrar todas las notas

    path('admin/', admin.site.urls), # Ruta para el panel de administración de Django

    path('ensayo/', views.ensayo, name='ensayo')
]

