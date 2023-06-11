from django.urls import path
from galeria.views import index, imagem

#Aqui pode ser entendido como o codigo de direcionamento das paginas HTML do nosso projeto
#Note que 

urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]