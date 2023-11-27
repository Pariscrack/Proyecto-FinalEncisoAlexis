from django.shortcuts import render,redirect
from .models import Blog,Comentario
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
import datetime
def ViewBlob(request):
    blog=Blog.objects.all()
    contexto={'blog':blog}
    return render(request, "blog.html",contexto)

def Detalle(request,id):
    user=False
    if request.user.is_authenticated and request.user.is_staff:
        user=True
    blog=Blog.objects.get(pk=id)
    comentarios=Comentario.objects.filter(blog=blog)
    return render(request,'detalle.html',{'blog':blog,'comentarios':comentarios,'user':user})

def SetComentario(request,id):
    if request.method=="POST":
        blog=Blog.objects.get(pk=id)
        autor=request.POST["autor"]
        comentario=request.POST["comentario"]
        fecha=datetime.datetime.now().date()
        coment=Comentario.objects.create(
            autor=autor,
            comentario=comentario,
            fecha=fecha,
            blog=blog
        )
        coment.save()
        messages.success(request,"Gracias por tu Comentario")
        return redirect("detalle",id=id)


def DeleteComentario(request,id):
    if request.method=="POST":
        blog=Blog.objects.get(pk=id)
        blog.imagen=None
        blog.save()
        return redirect("detalle",id=id)
    
def EditarComentario(request,id):
    if request.method=="POST":
        imagen=request.FILES.get('imagen')
        blog=Blog.objects.get(pk=id)
        blog.imagen=imagen
        blog.save()
        return redirect("detalle",id=id)

def About(request):
    user=request.user
    return render(request,"about.html",{'user':user})

def Logout(request):
    logout(request)
    return redirect('index')

def AboutSave(request):
    user=request.user
    user.username=request.POST['username']
    user.email=request.POST['email']
    user.first_name=request.POST['firstname']
    user.last_name=request.POST['lastname']
    user.save()

    return redirect("about")
