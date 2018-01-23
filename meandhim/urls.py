from django.conf.urls import url
from . import views

app_name = "meandhim"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/$', views.quiz, name='quiz'),
    
]
