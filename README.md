<h1><img src="https://cdn.discordapp.com/attachments/897304698468565022/932425051515551764/logo.png" alt="Logo Imobi" width="35px"> Imobi - PyStack Week 2.0</h1>

<p>Website - Agendamento de Imoveis com Python</p>

<h2>Sobre o Projeto</h2>
<p>
O projeto, foi desenvolvido na Semana PyStack Week 2.0, lecionado por <a href="https://www.linkedin.com/in/caio-sampaio-b08b8a17b"/> Caio Sampaio</a>.
<br>
Onde o objetivo do projeto, era criar uma aplicação web de <strong>Agendamento de Imoveis</strong>, com o framework <em>Django</em>.
<p>
  
<ul>
  <h3>Dentro do Backend</h3>
  <p>Padrão MVT (Model-View-Templates)</p>
  <li><strong>Model</strong> (Mapeamento do Banco de Dados): <br>
    <ul>
      <li> Para gerencimento de tabelas no banco de dados, foi utilizado a técnica <strong>ORM</strong> (Mapeamento objeto-relacional) que basicamente,
        transforma as classes Python em tabelas no banco de dados.</li>
    </ul>
    ➖ ➖ ➖ 
  </li>
  <li><strong>Template</strong> (Páginas para visualização de dados): <br>
    <ul>
    <li>Na seção <strong>Autenticação</strong>, o navegador irá renderizar a área de <strong>Cadastro</strong> e de <strong>Logar</strong></li>
    <li>Na seção <strong>Plataforma</strong> o navegador irá renderizar:</li>
      <ul>
        <li>A "home", com os imóveis dísponiveis;<br></li>
        <li>O "imovel", os próprios produtos, com imagem, descrição, localização e botão de agendamento;<br></li>
        <li>Os "agendamentos", haverá todos os imóveis que o usuário agendou.</li>
      </ul>
    </ul>
  </li>
  ➖ ➖ ➖ 
  <li><strong>View</strong> (Lógica de negócio): </li>
  <ul>
  <li>Nas Views de Autenticação e da Plataforma, comportará as funções, que irão realizar tarefas de requisições do usuário.</li>
  </ul>
    ➖ ➖ ➖ 
</ul>

## 

<h3>Para utilizar o Projeto: </h3>

- Python 3.9 instalado, ou verifique sua versão, caso já esteja instalado: python --version
- Instalar as Bibliotecas:
  - **Django** (Framework para desenvolvimento rápido para web)
  - **Pillow** (Biblioteca que adiciona suporte à abertura e gravação de muitos formatos de imagem diferentes)

```Python
# pip install django
# pip install pillow
```

*obs*: Caso de erro de ***csrf_token***, verifique se o seu navegador está aceitando cookies ou utilize outro navegador, aconselho utilizar o Google Chrome.<br><br>
Ou utilize já este usuário cadastrado, caso não esteja conseguindo:<br>
**username**: Caio<br>
**password**: 123

Para acessar a área de administração do **Django**:<br>
Na URL, do localhost, por exemplo http://127.0.0.1:8000 coloque, "/admin".<br>
**superuser**: admin<br>
**password**: imobi123

## 


<h2><img src="https://cdn.discordapp.com/attachments/897304698468565022/932425051515551764/logo.png" alt="Logo Imobi" width="35px"> Preview Imobi</h2>
