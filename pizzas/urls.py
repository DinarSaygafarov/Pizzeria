from django.conf.urls import url
from .import views

app_name = 'pizzas.urls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
