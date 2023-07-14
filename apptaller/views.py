from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactForm, AtencionForm, ModificarAtencionForm, ModificarMecanicoForm, MecanicoForm, CategoriaForm, PostulacionForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):

    mecanico = Mecanico.objects.all()

    mecanico = Mecanico.objects.raw("select * from apptaller_mecanico where vigente = true")

    data = {
        'mecanico':  mecanico,
        'form': ContactForm,
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = ContactForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Formulario guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, 'home.html', data)

def team(request):

    mecanico = Mecanico.objects.all()

    mecanico = Mecanico.objects.raw("select * from apptaller_mecanico where vigente = true")

    data = {
        'mecanico':  mecanico
    }
    
    return render(request, 'team.html', data)

def mostrar_atenciones(request):

    atencion = Atencion.objects.all()
    
    atencion = Atencion.objects.raw("select * from apptaller_atencion where aceptado = true")


    data = {
        'atencion':  atencion
    }

    
    if request.method == "POST":
        valor_buscado = request.POST.get("valor_buscado")   
        if valor_buscado != "":
            atencion = Atencion.objects.filter(categoria = valor_buscado)
            data["atencion"] = atencion
            #preguntar al profe como hacer para que solo muestre los aceptados al buscar por categoria

        else:
            data["atencion"] = Atencion.objects.raw("select * from apptaller_atencion where aceptado = true")
            
        
    return render(request, 'atenciones.html', data)

def contact(request):
    data = {
        'form': ContactForm,
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = ContactForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Formulario guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, 'contact.html', data)

def postulacion(request):
    data = {
        'formPost': PostulacionForm,
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = PostulacionForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Postulación guardada correctamente")
        else:
            data['formPost'] = formulario
            messages.success(request, "Ocurrio un error")

    return render(request, 'postulacion.html', data)


def listar_atencion(request):

    atencion = Atencion.objects.all()

    data = {
        'atencion': atencion
    }

    return render(request, "mantenedor/atencion/listar_atencion.html", data)

def modificar_atencion(request, diagnostico):
     
    atencion = get_object_or_404(Atencion, diagnostico=diagnostico)

    data = {
         "formAten": ModificarAtencionForm(instance=atencion)
    }

    if request.method == "POST":
        formulario = ModificarAtencionForm(data=request.POST, instance=atencion, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_atencion")
        else:
            data['formAten'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, "mantenedor/atencion/modificar.html", data)

def eliminar_atencion(request, diagnostico):
    atencion = get_object_or_404(Atencion, diagnostico=diagnostico)

    atencion.delete()

    return redirect(to=listar_atencion)



def login_usuario(request):

    
    print("Bienvenido: " + request.user.username)
    print("este es el login")

    #obtenemos todos los grupos al que pertenece el usuario 
    print('grupos:', request.user.groups.all())

    #validamos si el usuario pertenece a un grupo determinado
    if request.user.groups.filter(name='mecanico'):
        request.session["tipo"] = "mecanico"
        print("este es el proooo")
        
    else:
        request.session["tipo"] = "administrador"
        print("este es el addddd")

    return redirect(to='home')

def listar_mecanico(request):

    mecancio = Mecanico.objects.all()

    data = {
        'mecanico': mecancio
    }

    return render(request, "mantenedor/mecanico/listar_mecanico.html", data)

def eliminar_mecanico(request, rut):
    mecanico = get_object_or_404(Mecanico, rut=rut)

    mecanico.delete()

    return redirect(to=listar_mecanico)

def modificar_mecanico(request, rut):
     
    mecanico = get_object_or_404(Mecanico, rut=rut)

    data = {
         "formMeca": ModificarMecanicoForm(instance=mecanico)
    }

    if request.method == "POST":
        formulario = ModificarMecanicoForm(data=request.POST, instance=mecanico, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_mecanico")
        else:
            data['formMeca'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, "mantenedor/mecanico/modificar_mecanico.html", data)

def agregar_atencion(request):
    data = {
        'formAten': AtencionForm,
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = AtencionForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            mec = formulario.save(commit=False)
            mec.usuario = request.user

            mec.save()
            
            messages.success(request, "Atencion guardada correctamente")
        else:
            data['formAten'] = formulario
            messages.success(request, "Ocurrio un error")

    return render(request, 'mantenedor/atencion/agregar_atencion.html', data)

def agregar_mecanico(request):
    data = {
        'formMeca': MecanicoForm,
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = MecanicoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Formulario guardado"
        else:
            data['formMeca'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, 'mantenedor/mecanico/agregar_mecanico.html', data)

def registrar_usuario(request):

    data = {
        "mensaje" : ""
    }

    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Las contraseñas deben ser iguales!")
        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = correo
            usu.last_name = apellido
            usu.first_name = nombre
            grupo = Group.objects.get(name='mecanico')
        try:
            usu.save()
            usu.groups.add(grupo)
            messages.success(request, "Usuario registrado correctamente")

            
            return redirect(to='home')

        except:
            data["mensaje"] = 'error al grabar'

    return render(request, "registration/registro.html", data)

def agregar_categoria(request):
    data = {
        'formCat': CategoriaForm,
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = CategoriaForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoria guardada correctamente")
        else:
            data['formCat'] = formulario
            messages.success(request, "Ocurrio un error")

    return render(request, 'mantenedor/categoria/agregar_categoria.html', data)



def listar_postulacion(request):

    postulacion = Postulacion.objects.all()

    data = {
        'postulacion': postulacion
    }

    return render(request, "mantenedor/postulacion/listar_postulacion.html", data)

def detalle_atencion(request, pk):

    atencion = get_object_or_404(Atencion, pk=pk)

    data = {
        "a": atencion
    }
    
    return render(request, "detalle_atenciones.html", data)

def detalle_postulante(request, pk):

    postulacion = get_object_or_404(Postulacion, pk=pk)

    data = {
        "p": postulacion
    }
    
    return render(request, "detalle_postulante.html", data)
    

