12/07 🤖

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

ex: class = Links(models,Model):

    + e logo após criar as colunas da tabela que vc vai usar

    ex: link_redirecionado = models.urlsfield()
        link_encurtado = models.charField(max_length=10)

---

13/07 🤖

-> alterar o banco de dados para postgress
-> função para incluir a url curta (automaticamente) na base de dados
-> alterou o views para fazer o redirecionamento

    COMANDOS:
    + uuid.uuid4().hex[:8] - uuid é um modulo python que fornece um serviço de funções para hex, e logo em seguida inserimos o -hex- para definirmos a quantidade de caracter para a nossa url

        # mas afinal, o que é hex irmão ❓❔
        Hex (hexidecimal- números de 0 a 9 e letras de A até F) é um conjunto de letras e números aleatórios de comprimento fixo que são conhecidas por resumir um dado ou criptografar um segredo!!

        # uuid4() - Gera um uuid aleatório

    + def acha_minha_url(request, url_curta):
    site = Links.objects.get(url_curta=url_curta)
    return redirect(site.url_original)

        a nossa variavel -site- vai pegar pelo models o que definimos de url_curta, logo após ela faz a comparação com o banco de dados para ver se não há nenhuma url identica (caso haja ela não precisa fazer o trabalho novamente --ufa, um dia de folga 🎉 --)
        Após isso colocamos o -redirect- para que nossa url_curta seja redirecionada para o endereço da url_original, sendo assim, a pessoa verá o site desejado

    + docker-compose.yml: faça a criacão!!
        O Docker Compose ajuda a definir e compartilhar aplicativos de vários contêineres. Com o Docker Compose, você pode criar um arquivo para definir os serviços. Com um único comando, você pode criar tudo ou derrubá-lo.

    💱 mudando o banco para postegress 💱
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

    ⏫ subir banco ⏫

    abir um novo terminal, entrar na pasta do projeto e:

    + dar o docker ps para ver se tem algum outro banco rodando (e caso tenha, PARE-O IMEDIATAMENTE!!)

    + dar o docker-compose up

    deixar um terminal rodando o postgres

    + crie um SUPER usúario 🦸🏻‍♀️:

    rode o runserver

    -----------------------------------------
    15/07 fazendo a ligação do banco de dados e criando a o rederect 🤖:

    + Fizemos o redeirect (quando a pessoa clica na url vai direto pro site)

    + fizemos também a ligação com o banco para que o link encurtado aparecesse na tela

    --------------------------------
    18/07 🤖 -

    + Alterações no mobille do css
    + verificação no banco de dados
    -------------------------------------------------
    19/07 - 22/07 🤖

    + Ajustando alguns bugs

    + tirando a caixa cinza do css e deixando ela aparente apenas quando tiver uma url ou a mensagem de erro (uso de if):
    ______________________________________________________________________________________________________________________

    + na div mãe colocamos o seguinte comando: {% if request.method == 'POST' %} - que seria para ativar a caixa cinza quando tiver uma request (no nosso caso, essa request seria o aperto do botão)

    + {% if url_curta == none %} <p class="list_bloco_p">Insira uma URL válida :)</p>  --Esse comando seria para quando a url for vazia exibir mensagem de erro!!

    {% elif url_curta != '' %} - Já esse seria para fazer a exibição do proximo comando, que seria a url encurtada:

        <ul>
            <a target="_blank" href="{{ url_curta }}">https://myencurt.herokuapp.com/{{ url_curta }}</a>
        </ul>

    IMPORTANTE ❗❕: não enqueçam de sempre sechar um if com um {% endif %}!!!


    + deploy no heroku
    _______________________

    mas calma?? deploy?? como??? ☠️

    Primeiramente vamos entender, o que é deploy?? 🤟🏻 -
    O verbo deploy, em inglês, quer dizer implantar!! ou seja, faremos nossos usuarios finais finalmente terem acesso ao nosso site, em termos práticos, significa colocar no ar alguma aplicação que teve seu desenvolvimento concluído. De mesmo modo, quando um sistema sofre alguma melhoria ou alteração em seu código-fonte, implementar essa alteração ao sistema que está no ar também é um tipo de deploy.

    *ok, agora sim entendemos oq é esse raios de deploy, mas o que interresa é: COMO FAZ ISSO MEU DEUS 🙀?

    + criar um app no heroku (e sim essa é a hora mais dificil, a hora de decidir um nome extremamente legal!!!)

    +fazer o link do github (seu ortifolio) com o heroku -

[](../../../../../files-pri/T8DJ2DE76-F03QNP72QG3/image.png)

    + seleciona a branch que vc quer (sim, vocẽ é livre!🔓) e clica no botãozinho do build

    + faça o heroku login - é utilizado para autenticar seu usuário no CLI. O usuário utilizado é o que você criou ao se cadastrar.

    + aí você vai carregar os migrates para o heroku com o comanddo:
    heroku run python manage.py migrate --app nome_da_sua_app

    + então você vai configurar o seu postgres no heroku (colocando as variaveis do host, user, port, password... do seu projeto) - você consegue ver essas informações no seu arquivo .env e ele te entrega os seus "novos" valores

    + ai você clica novamente no botãozinho do build (seu grande amigo)

    + ai é só correr para o abraço 🎉 e clicar em open-app!!

    ❌ uma diquinha para evitar o corno_job ❌

    * habilite o build automatico no heroku!!!!

    ----------------------------------------------------------------------------------------------------
