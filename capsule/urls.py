from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index', name='index'),
    url(r'^add/', 'app.views.add', name='add'),
    url(r'^login_user/', 'app.views.login_user', name='login user'),
    url(r'^logout_user/', 'app.views.logout_user', name='logout user'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
