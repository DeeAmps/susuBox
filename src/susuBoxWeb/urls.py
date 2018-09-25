from django.conf.urls import url
from susuBoxWeb import urls
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about/', views.about, name="about"),
    url(r'^faq/', views.faq, name="faq"),
    url(r'^login/', views.login, name="login"),
    url(r'^register/', views.register, name="register"),
    url(r'^forgot/', views.forgot, name="forgot"),
    url(r'^terms/', views.terms, name="terms"),
    url(r'^privacy/', views.privacy, name="privacy"),
]
