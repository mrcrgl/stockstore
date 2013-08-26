from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stockstore.views.home', name='home'),
    # url(r'^stockstore/', include('stockstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'app.views.dashboard', name='dashboard'),

    url(r'^stock_search/$', 'app.views.stock_search', name='stock_search'),
    url(r'^add_stock/$', 'app.views.stock_add', name='add_stock'),

    url(r'^stock/(?P<symbol>\w+)/$', 'app.views.stock', name='stock'),
    url(r'^stock/(?P<symbol>\w+)/get_history/$', 'app.views.stock_fetch_history', name='stock_get_history'),
    url(r'^stock/(?P<symbol>\w+)/get_json/$', 'app.views.stock_rates_json', name='stock_rates_json'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='fe_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='fe_logout'),
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', name='fe_password_change'),
    url(r'^accounts/password_change_done/$', 'django.contrib.auth.views.login', name='password_change_done'),
)
