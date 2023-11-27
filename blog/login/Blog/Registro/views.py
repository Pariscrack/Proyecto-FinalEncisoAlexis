from django.shortcuts import render,redirect
from django.contrib.auth import models,authenticate,login
from  django.contrib import messages
from django.contrib.auth.hashers import make_password
from Blob.models import Blog
def Home(request):

    return render(request,'registrarse.html')
def ViewLogin(request):
    return render(request,'login.html')

def ViewPrincipal(request):
    blog=Blog.objects.order_by('-fecha')[:3]
    return render(request ,'principal.html',{'blog':blog})
def index(request):
    return redirect("login")
def Login(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["pass"]
        user=authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect("principal")
        else:
            messages.error(request,"User u Password Invalidos")
            return redirect("login")

   

def Register(request):
    if (request.method == "POST"):
        # Get form data
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["pass"]
        user_type = request.POST["tipo"]

        # Create a new user
        user = models.User.objects.create(
            username=username,
            email=email,
            
        )
        user.set_password(password)
        # Set user type to admin if selected
        if user_type == "admin":
            user.is_superuser= True
            user.is_staff=True
            # Save the user
            user.save()
        else:
            # Save the user
            user.save()

        

        # Display success message
        messages.success(request, "El Usuario se Ha registrado Correctamente.")

        # Redirect to home page
        return redirect("home")
