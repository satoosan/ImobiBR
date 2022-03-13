# ImobiBR - Projeto Semestral

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
- Banco de Dados (SQLite).

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
- ('/admin') -> Área do **Adminitrador**

##

Por default o **DEBUG** está como True, se caso trocar para False, usar o comando: 
```Python
 python manage.py runserver --insecure
```
Requirements necessary, Python 3.9 or higher. 

## 

## Referência 

Antigo <a href="https://github.com/satoosan/ImobiBR/tree/imobi---pystackweek">ImobiBR 1.0</a>
