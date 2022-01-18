import re
from django.http import HttpResponse
from django.shortcuts import render

from inventories.models import Good

# Create your views here.
def index(request):
    recently_updated_good_list = Good.objects.order_by("-update_date")[:5]
    context = {"recently_updated_good_list": recently_updated_good_list}
    return render(request, "inventories/index.html", context)


def detail(request, sku):
    return HttpResponse(f"You're looking at the information of good {sku}")
