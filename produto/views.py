from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from produto.models import Produto

class ListarProdutos(ListView):
   model = Produto
   template_name = 'produto/listar.html'
   context_object_name = 'produtos'



class DetalhesProdutos(View):
    pass

class AdicionarAoCarrinho(View):
    pass

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass

class Finalizar(View):
    pass
