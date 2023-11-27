from django.db import models

class Blog(models.Model):
    titulo=models.CharField(max_length=150)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to='images',null=True ,blank=True)
    descripcion=models.CharField(max_length=500 ,default="")
    autor=models.CharField(max_length=120)
    
    def __str__(self):
        return f'{self.titulo}'

class Comentario(models.Model):
    autor=models.CharField(max_length=120)
    comentario=models.CharField(max_length=600)
    fecha=models.DateField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.autor}{self.fecha}'
