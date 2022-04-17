from locale import strcoll
from turtle import title
from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article


def home_view(request):

    obj = Article.objects.get(id=2)
    query_set = Article.objects.all()
    # names = ['Carlos Soler', "Bruno Fernandes", "Harry Kane", "Lorenzon Pellegrine"]
    context = {
        'object_list': query_set,
        'id': obj.id,
        'title': obj.title,
        'content' : obj.content
    }
    html_string = render_to_string('home-view.html', context=context)

    return HttpResponse(html_string) 