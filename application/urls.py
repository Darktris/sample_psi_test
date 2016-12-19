from django.conf.urls import url
from application import views

urlpatterns = [
        url(r'^prescription$', views.prescription, name='prescription'),
        url(r'^$', views.prescription, name='prescription'),
]
