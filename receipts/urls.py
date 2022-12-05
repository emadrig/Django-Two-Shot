from django.urls import path
from receipts.views import receipt_list, my_receipt_list

urlpatterns = [
    path("", receipt_list, name="home"),
    path("mine/", my_receipt_list, name="my_receipt_list"),
    ]
