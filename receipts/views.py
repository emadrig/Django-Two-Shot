from django.shortcuts import render, redirect
from .models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm, CategoryForm, AccountForm
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
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()

            return redirect("home")

    else:
        form = ReceiptForm()
    context = {"form": form}
    return render(request, "receipts/create.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()

            return redirect("category_list")

    else:
        form = CategoryForm()
    context = {"form": form}
    return render(request, "categories/create.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()

            return redirect("account_list")

    else:
        form = AccountForm()
    context = {"form": form}
    return render(request, "accounts/create.html", context)
