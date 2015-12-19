from django.conf.urls import patterns, include, url
import views


urlpatterns = [


    url(r'^profile/$', views.user_profile, name='editprofile'),

]