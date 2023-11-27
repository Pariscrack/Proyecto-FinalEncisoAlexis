from django.urls import path
from .views import Home,Register,Login,ViewLogin,ViewPrincipal
urlpatterns=[
    path("",Home,name="home"),
    path("register",Register),
    path("login",ViewLogin,name="login"),
    path("signup",Login),
    path("principal",ViewPrincipal ,name="principal")
    

]