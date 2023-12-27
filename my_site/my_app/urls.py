from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('', views.simple_view, name="simple"),
    path('acercade', views.form_view, name="acercade"),
    path('<int:num_page>', views.num_page_view, name=""),
    path('<str:topic>', views.topic_view, name="topic-page"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.CustomLoginView.as_view(), name='login')
]