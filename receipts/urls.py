from django.urls import path
from receipts.views import (
    receipt_list,
    account_list,
    category_list,
    create_receipt,
)

urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
]
