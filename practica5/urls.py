from django.conf.urls import patterns, include, url




urlpatterns = patterns('',
    
    ('^home', 'static_page.views.home'),
    ('^help', 'static_page.views.help'),
    ('^about', 'static_page.views.about'),



    
)
