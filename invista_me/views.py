from django.shortcuts import render, redirect, HttpResponse # renderizar uma pagina HTML 
from .models import Investimento
from .froms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html', context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)}
    return render(request, 'investimentos/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        Investimento_form = InvestimentoForm(request.POST)
        if Investimento_form.is_valid():
            Investimento_form.save()
        return redirect('investimentos')
    else:    
        Investimento_form = InvestimentoForm()
        formulario = {
            'formulario': Investimento_form
        }
        return render(request,"investimentos/novo_investimento.html", context=formulario)

@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request,'investimentos/novo_investimento.html',{'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST,instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request,'investimentos/confirmar_exclusao.html',{'item':investimento})