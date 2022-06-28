from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('', views.simple_view, name="simple"),
    path('variable', views.form_view, name="variable"),
    path('<int:num_page>', views.num_page_view, name=""),
    path('<str:topic>', views.topic_view, name="topic-page"),
]