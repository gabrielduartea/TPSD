Trabalho Prático de Sistemas Distribuídos
      
Grupo: Alex Lopes, Gabriel Aguilar, Guilherme Rocha,   e Luiz Araújo.

Como executar uma API:

* Instale alguma versão do Python (3.5, 3.6, 3.7, 3.8, 3.9)
* Navegue até a pasta TPSD da API.
    * Ative a virtual env
        * Ativando em ambiente Unix: source env/bin/activate
    * Instale os pacotes:
        * pip install django
        * pip install djangorestframework
        * pip install markdown       # Markdown support for the browsable API.
        * pip install django-filter  # Filtering support
    * Execute o comando:
        * python manage.py migrate
    * Inicie o servidor
        * python manage.py runserver
    * Acesse localhost:8000/objetos
        * Para visualizar os objetos de aprendizagem em formato JSON selecione a opção "json" através do botão "GET"
        
