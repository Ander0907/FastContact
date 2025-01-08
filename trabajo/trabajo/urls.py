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

from django.contrib import admin
from django.urls import path
from contactos import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rutas principales
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.sign_off, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='mensaje.html'), name='mensaje'),

    # Rutas relacionadas con la gestión de contactos
    path('verinsert/', views.form_insert, name='verinsert'),
    path('formActualizar/<id>', views.form_update, name='formActualizar'),
    path('formNota/<id>', views.form_note, name='formNota'),

    # Rutas para operaciones CRUD de contactos.
    path('select/', views.select, name='select'),
    path('insert/', views.insert, name='insert'),
    path('update', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete'), 

    # Rutas relacionadas con la gestión de notas.
    path('insertNote/', views.insert_note, name='insertNote'),
    path('nota/', views.note, name='nota'),

    path('admin/', admin.site.urls),
]