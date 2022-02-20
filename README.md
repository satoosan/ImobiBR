<h1 align="center"><img src="https://cdn.discordapp.com/attachments/897304698468565022/932425051515551764/logo.png" alt="Logo Imobi" width="35px"> ImobiBR - Agendamentos de Imoves</h1>

<h3 align="center">🏢 Website - Agendamento de Imoveis desenvolvido com Python</h3>
<p align="center"><a href="#sobre">Sobre</a> ¤ <a href="#tech">Tecnologias</a> ¤ <a href="#tuto">Tutorial</a> ¤ <a href="#other">Outros</a></p>

##

<h2 id="sobre">✨ Sobre o Projeto</h2>
<div>
  <li> O Imobi foi re-criado, com a ideia de deixar o layout mais atraente e foi adicionado mais funcionalidades para os usuários.</li>
  <li> Foi criado com <b>Python</b> e o framework <b>Django</b>.</li>
  <li> Foi utilizado a tecnica ORM, em que a ideia é fazer com que as classes em Python, se transformem em tabelas no banco de dados.</li>
  <li> O banco padrão utilizado foi o SQLite.</li>
  <li> Foi utilizado o padrão MT<a href="#temp">¹</a>V.</li>
</div>
  
<h2 id="tech">💻 Tecnologias utilizadas</h2>

- **Python** e **Django**;
- Font Awesome 5 (Icons);
- Bootstrap 5;
- PIP (Gerenciador de Pacotes);
- VSCode (Editor de código-fonte);

##

<h2 id="tuto">✒ Tutorial</h2>

<h3>Pré-requisitos</h3>
<ul>
  <li>Python 3</li>
  <li>Git (Opcional)</li>
  <li>VSCode</li>
</ul>

<p>Clone este repositório, em seu diretório, ou faça download, por aqui, <a href="https://github.com/satoosan/Imobi-Pystackweek2.0/archive/refs/heads/main.zip">
  ImobiBR</a>.
</p>

```Bash
# Utilize esse comando no terminal, dentro do diretorio raíz.
python manage.py runserver
```
<p>Se caso der algum erro, de compilação, tenter abaixar primeiramente as libs.</p>

```Bash
pip install django
pip install pillow
```

Cadastre algum usuário, e depois logue com os mesmos dados que foram utilizados, se caso der algum erro de <b>_csrf</b>, de segurança, utilize o <b>ctrl+F5</b>, para atualizar e limpar o cache

##

<h2 id="outher">Outros</h2>

<h3> Acessar como <b>admin</b> </h3>
<p> Na URL, após o localhost, adicione "/admin", para acessar a área, após isso, irá solicitar um usuário e uma senha.</p>
<p> No terminal, novamente, utilize o comando </p>

```Bash
python manage.py createsuperuser
```

Segue as intruções, adicione um usuário e uma senha, qualquer outro dados é opcional.<br>
Dentro do formulário coloque os dados adicionados anteriormente, e voilá! Você agora é um super usuári.o</br>
Dentro do Django Admin, é possível, adicionar novas Ruas, Imoveis, Visitas e etc... Lembrando que isso pode influenciar no front-end. 

##

### Preview em Slides
<img src="https://github.com/satoosan/Imobi-Pystackweek2.0/blob/main/preview/preview.gif?raw=true" width="500px">
