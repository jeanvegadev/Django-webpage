from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from my_app.models import CustomUser
from my_app.forms import UsuarioForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

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
    usuarios = CustomUser.objects.all()
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'my_app/signup.html'

class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
    form_class = LoginForm
