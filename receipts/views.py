from django.shortcuts import render
from .models import Receipt

# Create your views here.


def receipt_list(request):
    receipt_list = Receipt.objects.all()
    context = {"receipt_list": receipt_list}

    return render(request, "receipts/list.html", context)

