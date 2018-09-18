from django.conf.urls import url
from . import views

app_name = 'food'

urlpatterns = [
    url(r'^order/$', views.order, name="order"),
    url(r'^$', views.homepage, name="home"),
    url(r'^prepare/$', views.prepare, name="prepare"),
    url(r'^success/$', views.success, name="success"),
    url(r'^orderlist/$', views.OrderList.as_view()),
    url(r'^orderdetail/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
]