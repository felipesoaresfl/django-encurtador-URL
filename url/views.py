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
        url_input = request.POST.get('url_input')
        url = Links.objects.create(url_original=url_input)
        url.save()

        url_curta = Links.objects.filter(url_original=url_input)
        return render(request, "url/index.html", {'url': url_curta})
    else:
        return render(request, "url/index.html")