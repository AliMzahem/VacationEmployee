from django.conf.urls import url
from django.contrib.auth import views

from Employee.views import register

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', register, name='register'),
]
