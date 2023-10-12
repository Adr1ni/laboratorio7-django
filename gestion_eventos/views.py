from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

def inicio(request):
    return render(request,'index.html')

def usuarios(request):

    usuarios = Usuario.objects.all()

    return render(request, 'usuario/total_usuario.html',{'usuarios': usuarios})


def crearUsuario(request):
    if request.method == 'GET':

        return render(request,'usuario/nuevo_usuario.html',{'form':UsuarioForm})
    else:
        try:
            form = UsuarioForm(request.POST)
            form.save()
            return redirect('usuarios')
        except ValueError:
            return render(request,'usuario/nuevo_usuario.html',{
                'form':UsuarioForm,
                'error':'Porfavor corrobore que los datos esten bien'
            })


def editarUsuario(request, usuario_id):
    
    if request.method == 'GET':
        usuario = get_object_or_404(Usuario,pk=usuario_id)
        form = UsuarioForm(instance=usuario)
        return render(request,'usuario/editar_usuario.html',{
            'form':form,
            'usuario':usuario
        })
    
    else:
        try:
            usuario = get_object_or_404(Usuario,pk=usuario_id)
            form = UsuarioForm(request.POST,instance=usuario)
            form.save()
            return redirect('usuarios')
        except ValueError:
            return render(request,'usuario/editar_usuario.html',{
            'form':UsuarioForm,
            'usuario':usuario,
            'error': 'Error al actulizar los datos'
        })


def eliminarUsuario(request, usuario_id):
    usuario = get_object_or_404(Usuario,pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect(usuarios)
    

def eventos(request):

    eventos = Evento.objects.all()

    return render(request, 'evento/total_evento.html',{'eventos': eventos})


def crearEvento(request):
    if request.method == 'GET':

        return render(request,'evento/nuevo_evento.html',{'form':EventoForm})
    else:
        try:
            form = EventoForm(request.POST)
            form.save()
            return redirect('eventos')
        except ValueError:
            return render(request,'evento/nuevo_evento.html',{
                'form':EventoForm,
                'error':'Porfavor corrobore que los datos esten bien'
            })


def editarEvento(request, evento_id):
    
    if request.method == 'GET':
        evento = get_object_or_404(Evento,pk=evento_id)
        form = EventoForm(instance=evento)
        return render(request,'evento/editar_evento.html',{
            'form':form,
            'evento':evento
        })
    
    else:
        try:
            evento = get_object_or_404(Evento,pk=evento_id)
            form = EventoForm(request.POST,instance=evento)
            form.save()
            return redirect('eventos')
        except ValueError:
            return render(request,'evento/editar_evento.html',{
            'form':EventoForm,
            'evento':evento,
            'error': 'Error al actulizar los datos'
        })


def eliminarEvento(request, evento_id):
    evento = get_object_or_404(Evento,pk=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect(eventos)


def registros(request):

    registros = RegistroEvento.objects.all()

    return render(request, 'registro/total_registro.html',{'registros': registros})


def crearRegistro(request):
    if request.method == 'GET':

        return render(request,'registro/nuevo_registro.html',{'form':RegistroEventoForm})
    else:
        try:
            form = RegistroEventoForm(request.POST)
            form.save()
            return redirect('registros')
        except ValueError:
            return render(request,'registro/nuevo_registro.html',{
                'form':RegistroEventoForm,
                'error':'Porfavor corrobore que los datos esten bien'
            })


def editarRegistro(request, registro_id):
    
    if request.method == 'GET':
        registro = get_object_or_404(RegistroEvento,pk=registro_id)
        form = RegistroEventoForm(instance=registro)
        return render(request,'registro/editar_registro.html',{
            'form':form,
            'registro':registro
        })
    
    else:
        try:
            registro = get_object_or_404(RegistroEvento,pk=registro_id)
            form = RegistroEventoForm(request.POST,instance=registro)
            form.save()
            return redirect('registros')
        except ValueError:
            return render(request,'registro/editar_registro.html',{
            'form':RegistroEventoForm,
            'registro':registro,
            'error': 'Error al actulizar los datos'
        })


def eliminarRegistro(request, registro_id):
    registro = get_object_or_404(RegistroEvento,pk=registro_id)
    if request.method == 'POST':
        registro.delete()
        return redirect(registros)