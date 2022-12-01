from django.shortcuts import render, redirect

from .models import Contacto
from .forms import Formulario
# Create your views here.


def index(request):
    return render(request,'agenda/index.html')


def page_contactos(request):
    query_contactos = Contacto.objects.all()
    return render(request, 'agenda/contactos.html', {'lista':query_contactos})


def page_add_contacto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        Contacto.objects.create(nombre = nombre,apellido=apellido,telefono=telefono)
        return redirect('list_contactos')
    return render(request, 'agenda/add_contact.html', {'formulario': Formulario()})


def page_detail_contacto(request):
    return render(request, 'adenda/detail_contact.html')
