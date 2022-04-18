from multiprocessing import context
from turtle import title
from venv import create
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

def article_create_view(request, *args, **kwargs): 
    context = {}
    if request.method == 'POST':
        form_data = request.POST
        title = form_data.get('title')
        content = form_data.get('content')
        article_obj = Article.objects.create(title=title, content=content)
        #ele cria esse objeto podemos armazena-lo em uma variavel e passar para a view
        context['created'] = True
        context['object'] = article_obj

    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None, *args, **kwargs):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)    
    context = {
        'object' : article_obj,
    }

    return render(request, "articles/detail.html", context=context)