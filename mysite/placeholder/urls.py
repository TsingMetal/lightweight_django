from django.conf.urls import url

from placeholder import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$',
        views.placeholder, name='placeholder'
       ),
]
