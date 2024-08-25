import shopify as Shopify
from django.shortcuts import render
from django.conf import settings
from shopify_auth import views as shopify_auth_views


# shopify.Session.setup(api_key=SHOPIFY_API_KEY, secret=API_SECRET)
# shopify.Product.find(1234)
# Create your views here.


def login(request):
    return shopify_auth_views.login(request)


def callback(request):
    return shopify_auth_views.callback(request)


def product_list(request):
    shop = Shopify(api_key=settings.SHOPIFY_API_KEY,
                   password=settings.SHOPIFY_API_SECRET, domain=request.session['shopify_admin'])
    products = shop.product.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, product_id):
    shop = Shopify(api_key=settings.SHOPIFY_API_KEY,
                   password=settings.SHOPIFY_API_SECRET, domain=request.session['shopify_admin'])
    product = shop.product.find(product_id)
    return render(request, 'product_detail.html', {'product': product})


def product_edit(request, product_id):
    shop = Shopify(api_key=settings.SHOPIFY_API_KEY,
                   password=settings.SHOPIFY_API_SECRET, domain=request.session['shopify_admin'])
    product = shop.product.find(product_id)
    return render(request, 'product_edit.html', {'product': product})
