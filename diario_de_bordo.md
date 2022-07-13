12/07

-> criar o repositório do 0 -
-> html e css básico

    COMANDOS:

    + criacão do ambiente virtual e ativação ( virtualenv .venv /// source .venv/bin/activate )

    + instalar o Django (pip install django) LEMBRE-SE DE ESTAR NO AMBIENTE VIRTUAL

    + django-admin startproject nome-do-projeto . (para iniciar o projeto) - coloque o . no final para o projeto ser criado na pasta atual

    + ./manage.py runserver (para aparecer o 🚀 -- voa moleque --)

    + pip freeze > requirements.txt

    + mudanças de linguagem no settings.py (deixar assim: TIME_ZONE= 'America/São paulo' e o 'LANGUAGE_CODE=pt-BR')

    + criar a app (./manage.py startapp nome-da-app)

    + cadastrar app no settings (procurar por installed_apps e coloca no final o 'nome-da-app')

    + criar uma class dentro de models
<<<<<<< Updated upstream
    ex: class = Links(models,Model):
=======
    ex: class= Links(models.Model):
>>>>>>> Stashed changes

    + e logo após criar as colunas da tabela que vc vai usar
    ex: link_redirecionado = models.urlsfield()
        link_encurtado = models.charField(max_length=10)

---

13/07

-> alterar o banco de dados para postgress
-> função para incluir a url curta (automaticamente) na base de dados
-> alterou o views para fazer o redirecionamento

    COMANDOS:
    + uuid.uuid4().hex[:8] - uuid é um modulo python que fornece um serviço de funções para hex, e logo em seguida inserimos o -hex- para definirmos a quantidade de caracter para a nossa url

        # mas afinal, o que é hex irmão ????
        Hex (hexidecimal- números de 0 a 9 e letras de A até F) é um conjunto de letras e números aleatórios de comprimento fixo que são conhecidas por resumir um dado ou criptografar um segredo!!

        # uuid4() - Gera um uuid aleatório

    + def acha_minha_url(request, url_curta):
    site = Links.objects.get(url_curta=url_curta)
    return redirect(site.url_original)

        a nossa variavel -site- vai pegar pelo models o que definimos de url_curta, logo após ela faz a comparação com o banco de dados para ver se não há nenhuma url identica (caso haja ela não precisa fazer o trabalho novamente --ufa, um dia de folga 🎉 --)
        Após isso colocamos o -redirect- para que nossa url_curta seja redirecionada para o endereço da url_original, sendo assim, a pessoa verá o site desejado

    ## mudando o banco ##
