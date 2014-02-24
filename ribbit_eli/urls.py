from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ribbit_eli.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','ribbit_eli_app.views.index'),
    url(r'^login$','ribbit_eli_app.views.login_view'),
    url(r'^logout$','ribbit_eli_app.views.logout_view'),
    url(r'^signup$','ribbit_eli_app.views.signup'),

    url(r'^admin/', include(admin.site.urls)),
)
