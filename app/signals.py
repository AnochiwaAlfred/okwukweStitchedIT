
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from orders.models import *
from orderhistory.models import *
from django.dispatch import receiver

@receiver(valid_ipn_received)
def payment_success_notification(request, sender, **kwargs):
    ipn_obj = sender
    print('IPN Valid')
    if ipn_obj.payment_status == ST_PP_COMPLETED:
         data = {
            'paymentMethod':request.POST.get('paymentMethod'), 
            'streetAddress':request.POST.get('streetAddress'), 
            'apartmentAddress':request.POST.get('apartmentAddress'),
            'state':request.POST.get('state'), 
            'city':request.POST.get('city'), 
            'country':request.POST.get('country'),
        }
         order = Order.objects.create(**data)
         user=request.user
         for item in user.cart.all():
            order.orderItems.add(item)
            item.reduce()
            item.save()
         order.save()
         if user.orderHistory==None:
            orderHistory=OrderHistory.objects.create()
            user.orderHistory=orderHistory
            user.save()
         user.orderHistory.orders.add(order)
         user.cart.clear()
         user.save()
         context={'message':'Purchase Successful'}
        
        
# @receiver(invalid_ipn_received)
# def payment_failed_notification(sender, **kwargs):
#     ipn_obj = sender
#     print('IPN Invalid')
#     if ipn_obj.payment_status == ST_PP_COMPLETED:
#         Order.objects.create()
        





















# from paypal.standard.models import ST_PP_COMPLETED
# from paypal.standard.ipn.signals import valid_ipn_received

# def show_me_the_money(sender, **kwargs):
#     ipn_obj = sender
#     if ipn_obj.payment_status == ST_PP_COMPLETED:
#         # WARNING !
#         # Check that the receiver email is the same we previously
#         # set on the `business` field. (The user could tamper with
#         # that fields on the payment form before it goes to PayPal)
#         if ipn_obj.receiver_email != "receiver_email@example.com":
#             # Not a valid payment
#             return

#         # ALSO: for the same reason, you need to check the amount
#         # received, `custom` etc. are all what you expect or what
#         # is allowed.

#         # Undertake some action depending upon `ipn_obj`.
#         if ipn_obj.custom == "premium_plan":
#             price = ...
#         else:
#             price = ...

#         if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'USD':
#             ...
#     else:
#         #...

# valid_ipn_received.connect(show_me_the_money)