from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redireciona para a página inicial ou outra página após o logout
    return render(request, 'usuarios/logout.html')

def novo_usuario(request):
    # tipo, validar, informar, salvar
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(
                request,f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
            '''
            messages.debug
            messages.info
            messages.success
            messages.warning
            messages.error
            '''
    else:
        formulario = UserRegisterForm()

    return render(request,'usuarios/registrar.html', {'formulario': formulario})
