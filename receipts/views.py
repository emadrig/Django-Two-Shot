from django.shortcuts import render, redirect
from .models import Receipt, ExpenseCategory, Account
from .forms import ReceiptForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def receipt_list(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {"receipt_list": receipt_list}

    return render(request, "receipts/list.html", context)


@login_required
def category_list(request):
    category_list = ExpenseCategory.objects.filter(owner=request.user)
    context = {"category_list": category_list}

    return render(request, "categories/list.html", context)


@login_required
def account_list(request):
    account_list = Account.objects.filter(owner=request.user)
    context = {"account_list": account_list}

    return render(request, "accounts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home")

    else:
        form = ReceiptForm()
    context = {"form": form}
    return render(request, "receipts/create.html", context)
