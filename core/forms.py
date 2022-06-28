from django import forms
from django.core.mail.message import EmailMessage
from django.db.models import fields

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        conteudo = f'Nome: {nome} , Email{email} Assunto: {assunto} Mensagem: {mensagem}'

        mail = EmailMessage (
            subject='Email enviado pelo sistema django',
            body=conteudo,
            from_email='contato@dominio.com',
            to=['contato@dominio.com'],
            headers={'Reply-To': email}
        )
        mail.send()