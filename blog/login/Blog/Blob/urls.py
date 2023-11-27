from django.urls import path
from .views import Logout,ViewBlob,Detalle,SetComentario,DeleteComentario,EditarComentario,About,AboutSave
urlpatterns=[
    path("",ViewBlob,name="blob"),
    path("detalle/<int:id>",Detalle,name="detalle"),
    path("saveComent/<int:id>",SetComentario , name="comentario"),
    path("deleteComent/<int:id>",DeleteComentario , name="delete_comentario"),
    path("editComent/<int:id>",EditarComentario , name="edit_comentario"),
    path("about/",About,name="about"),
    path("changeAbout/",AboutSave,name="saveabout"),
    path("logout/",Logout,name="logout"),



]
