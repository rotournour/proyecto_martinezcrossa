from django.shortcuts import render, redirect
from .models import Products 
from products.forms import ProductsForm
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test, login_required



def product_detail(request):
    products = Products.objects.all()
    return render(request, 'products/prueba.html', {'products': products})


#@login_required
def create_product (request):
    if request.method == 'GET':
        context = {
            'form': ProductsForm()}
        return render(request,'products/create.html', context=context)
    
    elif request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                idproduct=form.cleaned_data['idproduct'],
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                category = form.cleaned_data['category'],
                is_available = form.cleaned_data['is_available'],
                product_picture = form.cleaned_data ['product_picture']
                
            )
            context = {
                'message': 'Se ha cargado el producto'
            }
            return render(request, 'products/create.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductsForm()
            }
            return render(request, 'products/create.html', context=context)
        


def list_products(request):
    all_products = Products.objects.all()
    context = {
        'all_products':all_products
    }
    return render(request, 'products/list.html', context=context)

class UpdateProducts(LoginRequiredMixin, UpdateView):
    model = Products
    fields = ['price', 'is_available']  
    template_name = 'products/update.html'  
    success_url = '/products/list/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

class DeleteProducts (LoginRequiredMixin, DeleteView):
    model = Products
    template_name = 'products/delete.html'
    success_url = '/products/list/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])