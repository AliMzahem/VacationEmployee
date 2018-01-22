from django.conf.urls import url
from django.contrib.auth import views
urlpatterns=[
    url(r'^login/', views.login, name='login'),

]