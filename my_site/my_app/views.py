from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from my_app.models import Usuario
from my_app.forms import UsuarioForm
from django.contrib.auth.decorators import login_required

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

@login_required
def form_view(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_app:simple')) 
    else:
        form = UsuarioForm()
    
    return render(request, "my_app/form.html", context={"form": form})
