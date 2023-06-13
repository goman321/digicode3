from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http.response import HttpResponse


def clear_cache(request):
    try: 
        cache.clear()
        res = "ok"
    except:
        res = "err"
    return HttpResponse(res)

# @cache_page(60 * 15)
def index(request):
    return render(request, "pages/index.html")

# @cache_page(60*15)
def about_us(request):
    return render(request, "pages/about-us.html")

# @cache_page(60*15)
def contact(request):
    return render(request, "pages/contact.html")