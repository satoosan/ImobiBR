# ImobiBR - Projeto Semestral

Projeto feita na faculdade UNINOVE.

⚠ Muitas funcionalidades do site pararam de funcionar

1 - Cadastrar/Logar

2 - Algumas imagens estão com sua URL fora de ar

obs: Aqui está a visão geral de como era o Site por Completo

<p align="left">
  <a href="https://github.com/satoosan/ImobiBR/blob/main/overview/1-index.gif">Início</a> •
  <a href="https://github.com/satoosan/ImobiBR/blob/main/overview/2-login%26cadastro.gif">Sign/Log in</a> •
 <a href="https://github.com/satoosan/ImobiBR/blob/main/overview/3-home%26imovel.gif">Imoveis</a> •
 <a href="https://github.com/satoosan/ImobiBR/blob/main/overview/4-imovel%26agendamentos.gif">Agendamento</a>
</p>



### Integrantes 
- [ Guilherme Kimura](https://github.com/satoosan)
- [Luan Pereira](https://github.com/Luanc210)

## 

## Tecnoligias utlizadas: 
- LP Python;
- Framework Django;
- HTML, CSS e JS;
- Framework Bootstrap 4;
- JQuery;
- Editor de Codigo (Visual Studio Code);
- Icons (Font Awesome);
- Fonts (Google Fonts);
- Host Images (CDN Discord);
- Banco de Dados (SQLite);
- Chatbot (Landbot);
- PIP (Package Installer).

## 

## Tutorial

Instalar **libs**

```Python
pip install pillow
pip install python-decouple
```

### Connect Server 

```Python
# Usar o comando na raiz do projeto.
python manage.py runserver
```
### URLS

- ('/') -> **Página** Principal 
- ('/home') -> Paginação dos **Imoveis**
- ('/agendamentos') -> **Agendamentos** salvos
- ('/imovel/<str:id>') -> **Imoveis**
- ('/cadastro') -> Formulário de **Cadastro**
- ('/logar') -> Formulário de **Login**
- handler404 -> Página não encontrada
- handler50X -> Erro server
- ('/admin') -> Área do **Adminitrador**
- ('/privacy_policy') -> Privacidade política
- change password -> Criar uma nova senha

##

Por default o **DEBUG** está como True, se caso trocar para False, usar o comando: 
```Python
 python manage.py runserver --insecure
```
Requirements necessary, Python 3.9 or higher. 

Browser Support: Edge 11, Firefox, Chrome (better performance), Safari and Opera.
##

## Segurança da Informação  

### Validações
- Tamanho de caracteres
- Se os inputs das senhas são iguais
- Ter no mínimo um caracter especial
- A senha não pode ser igual ao usuário
- Verificação se o usuário ou o e-mail existem
- Captcha simples de input texto (com easter egg)

## Referência 

Antigo <a href="https://github.com/satoosan/ImobiBR/tree/imobi---pystackweek">ImobiBR 1.0</a>
