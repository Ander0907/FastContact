from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from contactos.models import Contactos
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Registro de usario
def sign_up(request):
    # Muestra la página de registro de usuarios si la solicitud es GET.
    if request.method == 'GET':
        return render(request, 'signup.html', { 
            'login_form': AuthenticationForm(),
            'signup_form': UserCreationForm()
        })
    else:
        # Comprueba si las contraseñas coinciden.
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Crea un nuevo usuario en la base de datos.
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save()
                # Inicia sesión para el nuevo usuario.
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    "error": "Este usuario ya existe"
                })
        return render(request, 'signup.html', {
            'error': 'Contraseñas no coinciden'
        })

# Inicio de sesión:
def sign_in(request):
    # Muestra la página de inicio de sesión si la solicitud es GET.
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'error': 'El usuario o contraseña es incorrecto'
            })
        else:
            # Inicia sesión para el usuario autenticado.
            login(request, user)
            return redirect('home')
        
# Cerrar sesión:
def sign_off(request):
    logout(request)
    return redirect('home')

def home(request):
    # Valida si el usuario está autenticado.
    if request.user.is_authenticated:
        # Crea un diccionario con parámetros para pasar a la plantilla.
        parametros = {'ver_contactos' : True, 'usuario': request.user.username}
    else:
        parametros = {}
    # Renderiza la plantilla de inicio con los parámetros adecuados según el estado de autenticación del usuario.
    return render(request, 'index.html', parametros)

@login_required
def form_insert(request):
    return render(request, 'insert.html')

@login_required
def form_update(request, id):
    # Obtiene el contacto con el ID especificado.
    resultado = Contactos.objects.get(id=id)
    return render(request, "update.html", {"resultados": resultado})

@login_required
def form_note(request, id):
    # Obtiene el contacto con el ID especificado.
    resultado = Contactos.objects.get(id=id)
    return render(request, "insert_note.html", {"resultados": resultado})

@login_required
def note(request):
    # Obtiene todos los contactos que tienen notas asociadas.
    contactos_con_notas = Contactos.objects.exclude(notas__isnull=True)
    return render(request, 'notas.html', {'resultados': contactos_con_notas})

@login_required
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

@login_required
def insert(request):
    nombre = request.POST['txtNombre']
    empresa = request.POST['txtEmpresa']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    # Crea un nuevo contacto en la base de datos.
    contacto = Contactos.objects.create(
       nombre=nombre, empresa=empresa, correo=correo, telefono=telefono, direccion=direccion)
    messages.success(request, '¡Persona registrada!')
    return redirect('select')

@login_required
def update(request):
    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    empresa = request.POST['txtEmpresa']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']

    contacto = Contactos.objects.get(id=id)
    contacto.id = id
    contacto.nombre = nombre
    contacto.empresa = empresa
    contacto.correo = correo
    contacto.telefono = telefono
    contacto.direccion = direccion 
    contacto.save()

    messages.success(request, '¡Persona Actualizada!')
    return redirect('select')

@login_required
def delete(request, id):
    # Obtiene el contacto con el ID especificado.
    persona = Contactos.objects.get(id=id) 
    persona.delete() 
    messages.success(request, '¡Persona eliminada!')
    return redirect('select')

@login_required
def insert_note(request):
    id = request.POST['txtId']
    titulo = request.POST['txtTitulo']
    nota = request.POST['txtNota']

    contacto = get_object_or_404(Contactos, id=id)
    contacto.notas = nota
    contacto.titulo_nota = titulo
    contacto.save()

    messages.success(request, '¡Persona registrada!')
    return redirect('nota')
