from django.shortcuts import render


from products.models import Product, ProductCategory
# Create your views here.


def index(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/index.html', context)


def about(request):
    return render(request, 'products/about.html')


def contacts(request):
    return render(request, 'products/contacts.html')
