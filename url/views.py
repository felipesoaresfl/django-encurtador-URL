from django.shortcuts import render
from django.shortcuts import redirect

import url

from .models import Links

# pega a url_curta no banco, para quando for inserida na barra de pesquisa 
# fazer o redirect para a url original 
def acha_minha_url(request, url_curta):
    site = Links.objects.get(url_curta=url_curta)

    return redirect(site.url_original)

