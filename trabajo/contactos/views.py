from django.contrib import messages  # Importa el módulo de mensajes de Django.
from django.shortcuts import render, redirect, get_object_or_404  # Importa funciones para renderizar vistas, redireccionar y obtener objetos 404.
from contactos.models import Contactos  # Importa el modelo de Contactos desde la aplicación contactos.
from django.utils import timezone  # Importa utilidades relacionadas con la zona horaria.
from django.contrib.auth import login, logout, authenticate  # Importa funciones relacionadas con la autenticación de usuarios.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Importa formularios de creación y autenticación de usuarios.
from django.contrib.auth.models import User  # Importa el modelo de usuarios de Django.
from django.db import IntegrityError  # Importa una excepción de Django para manejar errores de integridad en la base de datos.
from django.contrib.auth.decorators import login_required  # Importa el decorador para requerir autenticación en vistas específicas, sirve para proteger las rutas de usuarios no registrados.
from django.http import HttpResponse

# Registrar un usario:
def signup(request):
    if request.method == 'GET':  # Muestra la página de registro de usuarios si la solicitud es GET.
        return render(request, 'signup.html', { 
            'login_form': AuthenticationForm(),  # Crea un formulario de autenticación vacío.
            'signup_form': UserCreationForm()  # Crea un formulario de creación de usuario vacío.
        })
    else:
        if request.POST['password1'] == request.POST['password2']:  # Comprueba si las contraseñas coinciden.
            try:
                user = User.objects.create_user(  # Crea un nuevo usuario en la base de datos.
                    username=request.POST['username'],  # Obtiene el nombre de usuario del formulario.
                    password=request.POST['password1'],  # Obtiene la contraseña del formulario.
                )
                user.save()  # Guarda el usuario en la base de datos.
                login(request, user)  # Inicia sesión para el nuevo usuario.
                return redirect('home')  # Redirecciona al usuario a la página de inicio.
            except IntegrityError:
                return render(request, 'signup.html', {
                    "error": "Este usuario ya existe"  # Si ocurre un error de integridad, muestra un mensaje de error en la página de registro.
                })
        return render(request, 'signup.html', {
            'error': 'Contraseñas no coinciden'  # Si las contraseñas no coinciden, muestra un mensaje de error en la página de registro.
        })

# Iniciar sesión:
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')  # Muestra la página de inicio de sesión si la solicitud es GET.
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])  # Autentica al usuario.
        if user is None:
            return render(request, 'signin.html', {
                'error': 'El usuario o contraseña es incorrecto'  # Si la autenticación falla, muestra un mensaje de error en la página de inicio de sesión.
            })
        else:
            login(request, user)  # Inicia sesión para el usuario autenticado.
            return redirect('home')  # Redirecciona al usuario a la página de inicio.
        
# Cerrar sesión:
def sign_off(request):
    logout(request) # Cierra la sesión del usuario.
    return redirect('home') # Redirecciona al usuario a la página de inicio.

# Inicio:
def home(request):
    if request.user.is_authenticated: # Verifica si el usuario está autenticado.
        parametros = {'vercontactos' : True, 'usuario': request.user.username} # Crea un diccionario con parámetros para pasar a la plantilla.
    else:
        parametros = {}  # Si el usuario no está autenticado, no se pasa ningún parámetro adicional.
    return render(request, 'index.html', parametros)  # Renderiza la plantilla de inicio con los parámetros adecuados según el estado de autenticación del usuario.


# Formularios:
@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
def form_insert(request):
    return render(request, 'insert.html') # Renderiza el template 'insert.html' encargado de la inserción de contactos.

@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
def form_update(request, id):
    resultado = Contactos.objects.get(id=id) # Obtiene el contacto con el ID especificado.
    return render(request, "update.html", {"resultados": resultado}) # Renderiza el template 'update.html' para actualizar un contacto y pasa el contacto a la plantilla.

@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
def form_note(request, id):
    resultado = Contactos.objects.get(id=id) # Obtiene el contacto con el ID especificado.
    return render(request, "insert_note.html", {"resultados": resultado})  # Renderiza el template 'insert_note' para agregar una nota a un contacto y pasa el contacto a la plantilla.


@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
# Ver notas:
def note(request):
    contactos_con_notas = Contactos.objects.exclude(notas__isnull=True)  # Obtiene todos los contactos que tienen notas asociadas.
    return render(request, 'notas.html', {'resultados': contactos_con_notas})  # Renderiza la plantilla de notas y pasa los contactos con notas a la plantilla.


@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
# Operación listar(contactos):
def select(request):
    # Se inicializan las siguientes variables:
    contactos = None  # Esta variable almacena todos los contactos.
    nombre_busqueda = ''  # Esta variable almacena el nombre de búsqueda del contacto.
    contactos_encontrados = None  # Y esta variable almacena los contactos encontrados por la búsqueda.

    # Se Verifica el método de la solicitud (POST o GET).
    if request.method == 'POST':
        # Si la solicitud es POST, se procesa la búsqueda.
        nombre_busqueda = request.POST.get('nombre', '')  # Se obtiene el nombre de búsqueda del formulario.
        contactos_encontrados = Contactos.objects.filter(nombre__icontains=nombre_busqueda)  # Filtra los contactos que coinciden con el nombre de búsqueda
    else:
        # Si la solicitud no es POST, se obtienen todos los contactos.
        contactos = Contactos.objects.all()  # La variable contactos obtiene todos los contactos de la base de datos.

    # Se renderiza el template 'select.html' y pasa los datos necesarios.
    return render(request, 'select.html', {
        'contactos': contactos,  # Pasa todos los contactos obtenidos de la base de datos-
        'contactos_encontrados': contactos_encontrados,  # Pasa los contactos encontrados por la búsqueda.
        'nombre_busqueda': nombre_busqueda  # Pasa el nombre de búsqueda para mostrar en la plantilla.
    })


@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
# Operación insertar (contactos):
def insert(request):
    nombre = request.POST['txtNombre'] # Obtiene el nombre del contacto desde el template 'insert'.
    empresa = request.POST['txtEmpresa']  # Obtiene la empresa del contacto desde el template 'insert'.
    correo = request.POST['txtCorreo']  # Obtiene el correo del contacto desde el template 'insert'.
    telefono = request.POST['txtTelefono']  # Obtiene el telefono del contacto desde el template 'insert'.
    direccion = request.POST['txtDireccion']  # Obtiene la dirección del contacto desde el template 'insert'.

    contacto = Contactos.objects.create( # Crea un nuevo contacto en la base de datos.
       nombre=nombre, empresa=empresa, correo=correo, telefono=telefono, direccion=direccion)  # Asigna los valores obtenidos desde el template 'insert'.
    messages.success(request, '¡Persona registrada!') # Muestra un mensaje de éxito.
    return redirect('select') # Redirecciona a la página de selección de contactos.


@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
# Operación actualizar:
def update(request):
    id = request.POST['txtId'] # Obtiene el ID del contacto desde el template 'update'.
    nombre = request.POST['txtNombre']  # Obtiene el nombre del contacto desde el template 'update'.
    empresa = request.POST['txtEmpresa'] # Obtiene la empresa del contacto desde el template 'update'.
    correo = request.POST['txtCorreo'] # Obtiene el correo del contacto desde el template 'update'.
    telefono = request.POST['txtTelefono']  # Obtiene el telefono del contacto desde el template 'update'.
    direccion = request.POST['txtDireccion'] # Obtiene la dirección del contacto desde el template 'update'.


    contacto = Contactos.objects.get(id=id) # Obtiene el contacto con el ID especificado.
    contacto.id = id
    contacto.nombre = nombre # Actualiza el nombre del contacto.
    contacto.empresa = empresa  # Actualiza el nombre de la empresa del contacto.
    contacto.correo = correo # Actualiza el correo del contacto.
    contacto.telefono = telefono  # Actualiza el número de teléfono del contacto.
    contacto.direccion = direccion # Actualiza la dirección del contacto.
    contacto.save()  # Guarda los cambios en la base de datos.

    messages.success(request, '¡Persona Actualizada!')  # Muestra un mensaje de éxito.
    return redirect('select')  # Redirecciona a la página de selección de contactos.


@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
# Operación eliminar:
def delete(request, id):
    persona = Contactos.objects.get(id=id)  # Obtiene el contacto con el ID especificado.
    persona.delete()  # Elimina el contacto de la base de datos.
    messages.success(request, '¡Persona eliminada!')  # Muestra un mensaje de éxito.
    return redirect('select')  # Redirecciona a la página de selección de contactos.


@login_required # Asegura que la función solo sea accesible para usuarios autenticados.
# Operación insertar(notas):
def insert_note(request):
    id = request.POST['txtId'] # Obtiene el ID del contacto desde el template 'insert_note'.
    titulo = request.POST['txtTitulo']  # Obtiene el titulo de la nota desde el template 'insert_note'.
    nota = request.POST['txtNota']  # Obtiene el contenido de la nota para el contacto desde el template 'insert_note'.

    contacto = get_object_or_404(Contactos, id=id)   # Se obteniene el objeto Contactos con el ID proporcionado.
    contacto.notas = nota # Guarda la nota.
    contacto.titulo_nota = titulo # Guarda el titulo de la nota.
    contacto.save()  # Se guarda los cambios en la base de datos,

    messages.success(request, '¡Persona registrada!')  # Muestra un mensaje de éxito.
    return redirect('nota')  # Redirecciona a la página de visualización de notas.

def ensayo(request):
    return HttpResponse('Hola')