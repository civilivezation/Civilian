from django.conf.urls import patterns, url


from civ import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^home/',views.home,name='home'),
                       url(r'^game/',views.game,name='game'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^live/$', views.live, name='live'),
                       url(r'^user_info/$',views.user_info,name='user_info'),
)
