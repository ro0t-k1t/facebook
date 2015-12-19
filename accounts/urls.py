from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [

    url(r'^$', views.register_user),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^newsfeed/$', views.newsfeed, name="feed"),
    url(r'^accounts/register/$', views.register_user),

    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/register_success/$', views.register_success),

    url(r'^like/(?P<id2>\d+)/$', views.like, name="like"),
    url(r'^dislike/(?P<id2>\d+)/$', views.dislike, name="dislike"),

    url(r'^search/$', views.search_titles),

    #url(r'^like/$', views.like),

    url(r'^profile/(?P<id>\d+)/$', views.profile),
    url(r'^createfriend/(?P<id>\d+)/$', views.createfriendship, name="createfriend"),

    url(r'^createpoke/(?P<id>\d+)/$', views.createpoke, name="createpoke"),

    url(r'^accounts/invalid/$', views.invalid_login),




]