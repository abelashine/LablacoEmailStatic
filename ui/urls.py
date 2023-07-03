"""ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emailuis.views import *

urlpatterns = [
    path("", home, name=""),
    path("signup", signup, name="signup"),
    path("forget", forget, name="forget"),
    path("pt", product_transaction, name="pt"),
    path("ac", accepted, name="accepted"),
    path("rv", reviewed, name="reviewed"),
    path("of", offline, name="offline"),
    path("sw", swap, name=""),
    path("nfttr", nfttranscibtion, name=""),
    path("buygiveaway", buygiveaway, name=""),
    path("chatnotification",chatnotification),
    path("rentallastday",rentallastday),
    path("rentaldelaycharge",rentalchargedelay),
    path("rentaldelaychargebrand",rentalchargedelaybrand),
    path("rentalsuccessnotification",rentalSuccessNotification),

    # Subscription
    path("createsubscription",createsubscription),
    path("monthlysub",monthlysubscription),
    path("paymentfailedsub",paymentfailedsubscribtion),
    path("plancanceledsub",plancanceledsubscription),
    path("maximumuploadedsub",maximumuploadsubscription),


    
    path('admin/', admin.site.urls),
]
