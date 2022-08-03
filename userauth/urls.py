from django.urls import path
from . import views
<<<<<<< HEAD
from .views import CreateView, ListTheView, UpdateTheView, DeleteTheView, login
||||||| b4f0e7e
from .views import CreateView, ListTheView, UpdateTheView, DeleteTheView
=======
from .views import CreateView, ListTheView, UpdateTheView, DeleteTheView, logintest, testView, policyTest
>>>>>>> 85b93c6d051b8c19e01b0b2dc93af5126232d456
from django.views.generic import TemplateView


urlpatterns = [

    path("", views.CreateView.as_view(), name="Home"),
    path("list/", ListTheView.as_view()),
    path("<pk>/update", UpdateTheView.as_view()),
    path("<pk>/delete", DeleteTheView.as_view()),
    path("you", TemplateView.as_view(template_name='views/home.html')), # django default router
    path('<pk>/reset_password', views.reset_password_view, name='reset_password'),
<<<<<<< HEAD
    path('login/', views.login, name='loginform'),
    path('signup/', views.signup),

||||||| b4f0e7e
=======
    path("edit", views.testView, name="edit"),
    path("login", views.logintest,  name="login"),
    #Omolola's code below -- tope please fix.
    path("policy", views.policyTest, name="policy")
>>>>>>> 85b93c6d051b8c19e01b0b2dc93af5126232d456
]

