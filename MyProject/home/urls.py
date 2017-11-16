from django.conf.urls import url
from home.views import Homeview
from . import views

urlpatterns=[
    url(r'^$',Homeview.as_view(),name='home'),
    url(r'^connect/(?P<operator>.+)/(?P<pk>\d+)$',views.change_friend,name='change_friend'),
]