from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from django.conf import settings
from django.views.static import serve 

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    
    # 处理 media 信息，用于图片获取
    url(r'^files/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    
    
    url(r'^', include('account.urls')),
    #url(r'^$', RedirectView.as_view(url='/account/index/', query_string=True)),
    #url(r'^$', RedirectView.as_view(url='/login/', query_string=True)),
]
