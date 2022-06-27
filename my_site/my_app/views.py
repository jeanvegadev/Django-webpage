from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from my_app.models import Usuario

articles = {
    "sports": "deportes",
    "politics": "politica nacional",
    "education": "educacion en el peru"
}


# Create your views here.
def num_page_view(request, num_page):
    topic_list = list(articles.keys())
    topic = topic_list[num_page]

    webpage = reverse("topic-page",args=[topic])
    return HttpResponseRedirect(webpage)

def topic_view(request, topic):
    print("hola")
    try:
        topic = articles[topic]
        return HttpResponse("Usted eligio,"+ topic)
    except:
        raise Http404(topic)

def simple_view(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "my_app/example.html", context=context)

def variable_view(request):
    my_var = {
        'first_name':'jean',
        'last_name':'vega'
    }
    return render(request, "my_app/variable.html", context=my_var)
