from django.shortcuts import render 
#'Render' é um metodo de renderizacao de pagina html. Vamos usar ela para renderizar as pags
#Html que criarmos

# Create your views here. As 'Views' sao entendidas aqui como pags html 


def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')