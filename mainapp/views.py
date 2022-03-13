from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404
from django.http import Http404

current_user = User.objects.first()


def index(request):
    latest_ads = Ad.objects.order_by('-creation_date')
    context = {
        'latest_ads': latest_ads,
        'user': current_user
    }
    return render(request, 'index.html', context)


def item_info(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    context = {
        'ad': ad,
        'user': current_user
    }
    return render(request, 'item-info.html', context)


def my_items(request):
    my_ads = current_user.ad_set.all()
    context = {
        'my_ads': my_ads,
        'user': current_user
    }
    return render(request, 'my-items.html', context)


def edit_item(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    context = {
        'ad': ad,
        'user': current_user
    }
    return render(request, 'edit-item.html', context)
