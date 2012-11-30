from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from .views import *

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='gc_home'),
    url(r'^buy/$', Purchase.as_view(), name='gc_buy'),
    url(r'^subscribe/$', Subscribe.as_view(), name='gc_subscribe'),
    url(r'^preauth/$', Preauth.as_view(), name='gc_preauth'),
    url(r'^confirm/$', Confirm.as_view(), name='gc_confirm'),
    url(r'^success/$', Success.as_view(), name='gc_success'),
    url(r'^error/$', Error.as_view(), name='gc_error'),
    url(r'^webhook/$', Webhook.as_view(), name='gc_webhook'),
)
