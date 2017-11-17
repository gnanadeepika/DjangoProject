from django.conf.urls import url,include
from django.contrib import admin
from .views import login_redirect
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/',include('account.urls',namespace='account')),
    url(r'^home/',include('home.urls',namespace='home')),
    url(r'^$',login_redirect,name='login_redirect')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
