from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

import re

# libs send email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect('/auth/cadastro')
        elif re.findall(username.lower(), senha.lower()):
            messages.add_message(request, constants.ERROR,
                                 'Senha não pode ser igual ao usuario')
            return redirect('/auth/cadastro')
        
        elif re.findall('123', senha) or re.findall('234', senha) or re.findall('345', senha) or re.findall('456', senha) or re.findall('567', senha) or re.findall('678', senha) or re.findall('789', senha):
            messages.add_message(request, constants.ERROR,
                                 'Senha não pode ter uma sequencia numérica')
            return redirect('/auth/cadastro')
        
        elif senha != confirmar_senha:
            messages.add_message(request, constants.ERROR,
                                 'As senhas digitadas não são iguais!')
            return redirect('/auth/cadastro')
        
        elif len(senha.strip()) <= 5:
            messages.add_message(request, constants.ERROR,
                                'A senha tem que ter no minimo 6 caracteres e ao menos um caracter especial')
            return redirect('/auth/cadastro')
        
        elif re.search('[,.;@/]', senha.strip()) == None:
            messages.add_message(request, constants.ERROR,
                                'A senha tem que ter no minimo 6 caracteres e ao menos um caracter especial (@ / . , ;)')
            return redirect('/auth/cadastro')
        
        user = User.objects.filter(username=username)
        email_filter = User.objects.filter(email=email)
        
        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 'Já existe um usuario com esse nome cadastrado')
            return redirect('/auth/cadastro')
        
        #deu certo
        if email_filter.exists():
            messages.add_message(request, constants.ERROR,
                                 'Esse email já foi cadastrado')
            return redirect('/auth/cadastro')
        
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha)
            user.save()

            messages.add_message(request, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso!')

            # Send E-mail
            html_content = render_to_string('emails/cadastro_confirmado.html')
            text_content = strip_tags(html_content)

            email_send = EmailMultiAlternatives(
                    'Cadastro Confirmado', text_content, settings.EMAIL_HOST_USER, [email])
            email_send.attach_alternative(html_content, 'text/html')
            email_send.send()

            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR,
                                 'Erro interno do sistema')
            return redirect('/auth/cadastro')


def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/home.html')
        return render(request, 'logar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)
        if not usuario:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            
            # Send e-mail
            html_content = render_to_string('emails/promo_imovel.html')
            text_content = strip_tags(html_content)

            email_send = EmailMultiAlternatives(
                'Bem vindo ao ImobiBR', text_content, settings.EMAIL_HOST_USER, [usuario.email])
            email_send.attach_alternative(html_content, 'text/html')
            email_send.send()
        return redirect('/home')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')


def handler404(request, exception):
    return render(request, 'status_code/not_found.html')


def handler500(request):
    return render(request, 'status_code/server_error.html')
