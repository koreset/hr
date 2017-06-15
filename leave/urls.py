# We are adding a URL called /home
from django.conf.urls import url

from leave import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
