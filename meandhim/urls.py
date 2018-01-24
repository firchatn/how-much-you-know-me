from django.conf.urls import url
from . import views

app_name = "meandhim"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[-\w]+)/(?P<val>[-\w]+)/(?P<id>[-\w]+)$', views.quiz, name='quiz'),
    url(r'^(?P<name>[-\w]+)/result$', views.result, name='result'),
    url(r'^(?P<name>[-\w]+)/share$', views.share, name='share'),
    
]
