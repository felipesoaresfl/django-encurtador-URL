from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect

import url

from .models import Links

# pega a url_curta no banco, para quando for inserida na barra de pesquisa 
# fazer o redirect para a url original 
def acha_minha_url(request, url_curta):
    site = Links.objects.get(url_curta=url_curta)

    return redirect(site.url_original)

def pagina_inicial(request):
    if request.method == "POST":
        #pega o que foi digitado no input
        url_input = request.POST.get('url_input')
        if url_input != '':
            url_existente = Links.objects.filter(url_original=url_input).first()
            if url_existente: 
                if url_existente.url_original == url_input:
                    context = {
                        'url_curta': url_existente.url_curta,
                    }
                else:
                    url_curta = Links.objects.create(url_original=url_input)
                    url_curta.save()
                    context ={
                        'url_curta': url_curta.url_curta,
                    }
                
            else:
                url_curta = Links.objects.create(url_original=url_input)
                url_curta.save()
                context ={
                    'url_curta': url_curta.url_curta,
                }
            return render(request, "url/index.html", context)
    return render(request, "url/index.html")