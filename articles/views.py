from multiprocessing import context
from django.http import QueryDict
from django.shortcuts import render
from .models import Article

# Create your views here.

def article_search_view(request, *args, **kwargs):
    query_dict = request.GET
    #query = query_dict.get('query') #valor do input name
    try:
        query = int(query_dict.get('query'))
    except:
        query = None

    article_obj = None

    if query is not None:
        article_obj = Article.objects.get(id=query)    
        
    context ={
        'object' : article_obj
    }
    return render(request,"articles/search.html", context=context)


def article_detail_view(request, id=None, *args, **kwargs):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)    
    context = {
        'object' : article_obj,
    }

    return render(request, "articles/detail.html", context=context)