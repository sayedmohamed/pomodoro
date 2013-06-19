from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
	url(r'^timer', 'app.views.timer', name='timer'),
	url(r'^history', 'app.views.history', name='history'),
	url(r'^tasks/new', 'app.views.tasksNew', name='tasksNew'),
	url(r'^tasks', 'app.views.tasks', name='tasks'),
	url(r'^login', 'app.views.login', name='login'),
    # url(r'^pomodoro/', include('pomodoro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
