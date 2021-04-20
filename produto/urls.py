from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('',views.ListarProdutos.as_view(), name = 'listarProduto'),
    path('<slug>', views.DetalhesProdutos.as_view(), name='detalhesProduto'),
    path('adicionaraoCarinho', views.AdicionarAoCarrinho.as_view(), name='adicionarCarrinho'),
    path('removerdoCarrinho', views.RemoverDoCarrinho.as_view(), name='removerProduto'),
    path('carrinho', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar', views.Finalizar.as_view(), name='finalizar'),

]