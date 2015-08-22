from django.conf.urls import include, url
from django.contrib import admin
from comments_demo.views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'comments_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
]
