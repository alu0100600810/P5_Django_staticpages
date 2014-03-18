from django.conf.urls import patterns, include, url




urlpatterns = patterns('',
    
 

    url('^home', 'static_page.views.home', name='home'),
   # ('^help', 'static_page.views.help'),
   # ('^about', 'static_page.views.about'),



    
)
