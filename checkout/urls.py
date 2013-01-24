from django.conf.urls.defaults import *
from ecomstore import settings

urlpatterns = patterns('checkout.views',
    #===========================================================================
    # (r'^$', 'show_checkout', {'template_name': 'checkout/checkout.html',
    #    'SSL':settings.ENABLE_SSL}, 'checkout'),
    # (r'^receipt/$', 'receipt', {'template_name': 'checkout/receipt.html',
    #    'SSL': settings.ENABLE_SSL}, 'checkout_receipt'),)
    #===========================================================================
    (r'^$', 'show_checkout', {'template_name': 'checkout/checkout.html'}, 
        'checkout'),
    (r'^receipt/$', 'receipt', {'template_name': 'checkout/receipt.html'}, 
        'checkout_receipt'),)    