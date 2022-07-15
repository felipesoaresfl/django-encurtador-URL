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

> > > > > > > Stashed changes

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

    + docker-compose.yml: faça a criacão!!
        O Docker Compose ajuda a definir e compartilhar aplicativos de vários contêineres. Com o Docker Compose, você pode criar um arquivo para definir os serviços. Com um único comando, você pode criar tudo ou derrubá-lo.

    ## mudando o banco para postegress ##
    + encontrar databases dentro de -settigs.py-

    + importar o Os - para importar as variavies de ambiente do .env
    + dotenv- para ler o par de chave (secret-key), comparando a secret key que tem o settings com a que tem no .env e após essa comparação ele autoriza a usar a usar as variaveis de ambiente que você criou dentro o .env

    + crie um arquivo .env com as seguintes variaveis:

    DEBUG=True
    SECRET_KEY='escolha-uma-secret-key'
    POSTGRES_DB= escolha_o_nome_do_seu_banco
    POSTGRES_USER= escolha_o_usuario_do_seu_banco
    POSTGRES_PASSWORD= escolha_sua_senha
    POSTGRES_HOST= localhost
    POSTGRES_PORT= 55432 - está porta foi escolhida para que não haja conflito caso você tenha o postgres instalado na sua máquina!!

    + instalar psycopg2 - para que o python consiga reconhecer o banco de dados postgres

    + dar o pip install python-dotenv

    + dar o pip freeze > requirements

    + ctrl r = atalho para rodar runserver

    # subir banco #

    abir um novo terminal, entrar na pasta do projeto e:

    + dar o docker ps para ver se tem algum outro banco rodando (e caso tenha, PARE-O IMEDIATAMENTE!!)

    + dar o docker-compose up

    deixar um terminal rodando o postgres

    + crie um SUPER usúario 🦸🏻‍♀️:

    rode o runserver

    -----------------------------------------
    15/07 fazendo a ligação do banco de dados e criando a ligação:

    +
