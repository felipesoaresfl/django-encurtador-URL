12/07

-> criar o repositório do 0 -
-> html e css básico

    COMANDOS:

    + criacão do ambiente virtual e ativação ( virtualenv .venv /// source .ven/bin/activate )

    + instalar o Django (pip install django) LEMBRE-SE DE ESTAR NO AMBIENTE VIRTUAL

    + django-admin startproject nome-do-projeto . (para iniciar o projeto) - coloque o . no final para o projeto ser criado na pasta atual

    + ./manage.py runserver (para aparecer o 🚀 -- voa moleque --)

    + pip freeze > requirements.txt

    + mudanças de linguagem no settings.py (deixar assim: TIME_ZONE= 'America/São paulo' e o 'LANGUAGE_CODE=pt-BR')

    + criar a app (./manage.py startapp nome-da-app)

    + cadastrar app no settings (procurar por installed_apps e coloca no final o 'nome-da-app')

    + criar uma class dentro de models
    ex: class = Links(models,Model):

    + e logo após criar as colunas da tabela que vc vai usar
    ex: link_redirecionado = models.urlsfield()
        link_encurtado = models.charField(max_length=10)
