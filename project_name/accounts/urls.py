from django.conf.urls import include, url,patterns

urlpatterns = patterns('',
    url(r'^$', 'project_name.accounts.views.dashboard', name='dashboard'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
    	{'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', 
    	{'next_page': 'core:home'}, name='logout'),
    url(r'^criar-conta/$', 'project_name.accounts.views.register', name='register'),
)