from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse   # added

def home(request):
    return render(request,'routes.html')
def signup(request):
    return render(request,'sign-up-confirmation.html')
def forget(request):
    return render(request,'forgot-password.html')
def product_transaction(request):
    return render(request,'product_transaction_receipt_brand.html')
def accepted(request):
    return render(request,'business-accepted.html')
def reviewed(request):
    return render(request,'business-review.html')
def offline(request):
    return render(request,'business-offline.html')
def swap(request):
    return render(request,'swap_request_brand.html')

def nfttranscibtion(request):
    return render(request,'nft_transaction_receipt_brand.html')
def buygiveaway(request):
    return render(request,'buy-giveaway-confirm.html')
def chatnotification(request):
    return render(request,'chat_notifications.html')

def rentallastday(request):
    return render(request,'rent_notification_last_day.html')
def rentalchargedelay(request):
    return render(request,'rent_notification_charge_delay.html')
def rentalchargedelaybrand(request):
    return render(request,'rent_notification_charge_delay_brand.html')
def rentalSuccessNotification(request):
    return render(request,'rent_notification_success_return.html')

def createsubscription(request):
    return render(request,'create_subscription_template.html')
def monthlysubscription(request):
    return render(request,'monthly_subscription_template.html')
def paymentfailedsubscribtion(request):
    return render(request,'payment_failed.html')
def plancanceledsubscription(request):
    return render(request,'plan_canceled_automatically.html')
def maximumuploadsubscription(request):
    return render(request,'reaching_max_uploads.html')