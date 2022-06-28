from django.shortcuts import redirect, render
from .forms import ContatoForm
from django.contrib import messages

def index(request):
    form = ContatoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            '''nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']'''

            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForm()
        else:
           messages.error(request, 'Erro ao enviar e-mail')

    context= {
        'form': form
    }
    return render(request,  'index.html', context)