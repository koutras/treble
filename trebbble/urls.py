from django.conf.urls import patterns, include, url
from trebble import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trebbble.views.home', name='home'),
    # url(r'^trebbble/', include('trebbble.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	(r'^company-list$', views.show_company_list),
	(r'^company/(?P<company_id>\d+)/$', views.show_company),
	(r'^add-company/$', views.add_company),
	
)
