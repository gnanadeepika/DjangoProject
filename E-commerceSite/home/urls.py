from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^$',views.IndexView.as_view(),name="index"),
                url(r'^details/(?P<pk>\d+)$',views.ProductDetailView.as_view(),name="detail"),
                url(r'^cart/$',views.CartView.as_view(),name="cart"),
                url(r'^remove/(?P<pk>\d+)/$',views.delete_product,name="delete_product"),
              ]