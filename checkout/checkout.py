#import google_checkout
import authnet
from cart import cart
from models import Order, OrderItem
from forms import CheckoutForm
from ecomstore import settings
from django.core import urlresolvers
import urllib

def get_checkout_url(request):
    return urlresolvers.reverse('checkout')

def process(request):
    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_HOR_REVIEW = '4'
    postdata = request.POST.copy()
    card_num = postdata.get('credit_card_number','')
    exp_month = postdata.get('credit_card_expire_month','')
    exp_year = postdata.get('credit_card_expire_year','')
    exp_date = exp_month + exp_year
    cvv = postdata.get('credit_card_cvv', '')
    amount = cart.cart_subtotal(request)
    results = {}
    responce = authnet.do_auth_capture(amount=amount, card_num=card_num, 
                    exp_date=exp_date, card_cvv=cvv)
    if responce[0] == APPROVED:
        transaction_id = responce[6]
        order = create_order(request, transaction_id)
        results = {'order_number':order.id,'message':''}
    if responce[0] == DECLINED:
        results = {'order_number':0,
                   'message':'There is a problem with your credit card.'}
    if responce[0] == ERROR or responce[0] == HELD_HOR_REVIEW:
        results = {'order_number':0,'message':'Error processing order.'}
    return results

def create_order(request,transaction_id):
    order = Order()
    checkout_form = CheckoutForm(request.POST, instance=order)
    order = checkout_form.save(commit=False)
    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED
    order.save()
    
    if order.pk:
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.save()
        cart.empty_cart(request)
        if request.user.is_authenticated():
            from accounts import profile
            profile.set(request)
    return order
    