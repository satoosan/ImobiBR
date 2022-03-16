from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# libs email
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

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 'Já existe um usuário com esse nome cadastrado')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha)

            user.save()

            messages.add_message(request, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso!')
            
            html_content = render_to_string('emails/cadastro_confirmado.html')
            text_content = strip_tags(html_content)
            
            email_send = EmailMultiAlternatives('Cadastro Confirmado', text_content, settings.EMAIL_HOST_USER, [email])
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

        print(senha)

        if not usuario:
            messages.add_message(request, constants.ERROR,
                                 'Username ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/home')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')


def handler404(request, exception):
    return render(request, 'status_code/not_found.html')

def handler500(request):
    return render(request, 'status_code/server_error.html')