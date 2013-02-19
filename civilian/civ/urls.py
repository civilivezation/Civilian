from django.conf.urls import patterns, url

from civ import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^home/',views.home,name='home'),
                       url(r'^game/',views.game,name='game'),
                       url(r'^register/$', views.register, name='register'),
)
