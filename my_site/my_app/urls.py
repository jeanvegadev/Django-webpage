from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('', views.index, name=""),
    path('simple', views.simple_view, name="simple"),
    path('variable', views.variable_view, name="var"),
    path('<int:num_page>', views.num_page_view, name=""),
    path('<str:topic>', views.topic_view, name="topic-page"),
]