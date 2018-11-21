from django.conf.urls import  url
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from myApp import views
urlpatterns = [
    url(r'^myApp/', include('myApp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^special/', views.special, name='special'),
    url(r'^logout/$', views.user_logout, name='logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)