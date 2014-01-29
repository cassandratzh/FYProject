from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TGFB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #on a domain name watever infront of admin
    url(r'^$', 'cancer.views.mainpage'), #watever domain name is local host or wat. main directory to index view then go to index.html template
    url(r'^cancer/', 'cancer.views.cancersite'),
    url(r'^smads/', 'cancer.views.smadsite'),
    url(r'^targetedgenes/', 'cancer.views.genesite'),
    

)
