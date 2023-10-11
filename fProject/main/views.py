from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    nameFilter = request.GET.get("nameFilter")
    if nameFilter:
        products = products.filter(name__contains=nameFilter)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def create(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
    if(form.is_valid()):
        form.save()
        return render(request, 'shop/product/list.html')

    context = {
        'form': form
    }
    return render(request, 'shop/product/add.html', context)


def update(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        post = request.POST.copy()
        slider1_val = int(request.POST.get('storage1'))
        slider2_val = int(request.POST.get('storage2'))
        post['unallocated'] = int(post['stock']) - slider1_val - slider2_val
        request.POST = post
        form = ProductForm(request.POST, request.FILES, instance=product)
        if(form.is_valid()):
            form.save()
            return render(request, 'shop/product/list.html')

    context = {
        'form': form
    }

    return render(request, 'shop/product/update.html', context)


def delete(request, pk):
    object = Product.objects.filter(pk=pk)
    object.delete()
    return render(request, 'shop/product/list.html')