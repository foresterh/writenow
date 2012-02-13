from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
            url(r'^$', 'login',
                {'template_name': 'login.html'},
                name='login'),
            url(r'^login/$',
                'login', {'template_name': 'login.html'},
                name='login'),
            url(r'^logout/$',
                'logout', {'next_page': '/'},
                name='logout'),
            url(r'^password_change/$',
                'password_change',
                name='password_change'),
            url(r'^password_change/done/$',
                'password_change_done',
                name='password_change_done'),
        )