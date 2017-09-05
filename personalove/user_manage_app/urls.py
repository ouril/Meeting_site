from django.conf.urls import url
from .views import (
    login,
    logout,
    registration,
    find_somebody,
    make_account,
    UserAccountDetailView,
    filter
)

urlpatterns = [
    url(r'^$', find_somebody, name='main'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^filter/$', filter, name='filter'),
    url(r'^detail/(?P<pk>\d+)/$', UserAccountDetailView.as_view(), name='detail'),
    url(r'^make_account/$', make_account, name='make_account'),
    url(r'^registration/$', registration, name='registration')
]