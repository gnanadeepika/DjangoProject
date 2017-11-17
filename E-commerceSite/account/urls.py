from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [
                  url(r'^login/$',login,{'template_name':'account/login.html'},name="login"),
                  url(r'^logout/$',logout,{'template_name':'account/logout.html'},name="logout"),
                  url(r'^home/$',views.HomeView.as_view(),name="home"),
                  url(r'^register/$',views.Register.as_view(),name="register"),
                  url(r'^profile/$',views.view_profile,name="view_profile"),
                  url(r'^edit-profile/$',views.edit_profile,name="edit_profile"),
                  url(r'^change-password/$',views.change_password,name="change_password")
              ]