from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import logout, login







urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
]