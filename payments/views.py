from datetime import time
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, reverse, redirect, get_object_or_404
import stripe
from .models import Pay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Pay
from Houses.models import House_Details
from accounts.models import User_Profile


# Create your views here.
@login_required
def payment_process(request, id=id):
    user_id = request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items = [
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': House_Details.id,
                        },
                        'unit_amount': 300,
                    },
                    'quantity': 1,
                }
            ],
            mode = 'payment',
            success_url = request.build_absolute_uri(reverse('payments:completed')) + 'session_id={CHECKOUT_SESSION_ID}',
            cancel_url = request.build_absolute_uri(reverse('payments:canceled')),
        )
        
        return redirect(checkout_session.url, code=303)
    return render(request, 'payment/process.html')

def payment_completed(request):
    #session_id = request.GET.get('session_id')
    #if session_id is None:
    #    return HttpResponseNotFound()
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_id = request.User.user_id
    user_payment = Pay.objects.get(user=user_id)
    user_payment.stripe_checkout_id = checkout_session_id
    user_payment.save()
    Pay.payment_bool = True
    
    return render(request, 'payment/completed.html', {'customer': customer})

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
@csrf_exempt
def stripe_webhook(request, id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    time.sleep(10)
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get(id=id)
        time.sleep(15)
        user_payment = Pay.objects.get(stripe_checkout_id=session_id)
        line_items = stripe.checkout.session.list_line_items(session_id, limit=1)
        user_payment.payment_bool = True
        user_payment.save()
    return HttpResponse(status=200)
