# In The Name Of God 
# Creation Date : 3/11/17
# Created By : Mahtab Farrokh (mahtab.farrokh@gmail.com)

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]