from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product,CartDetails
from .forms import AddToCartForm
# Create your views here.

class IndexView(ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()

class CartView(TemplateView):
    template_name = 'home/cart.html'
    def get(self,request):
        cartProducts=CartDetails.objects.filter(cuser=request.user)
        total=0
        for line in cartProducts:total+=line.quantity*line.cproduct.price
        return render(request,self.template_name,{'cartProducts':cartProducts,'total':total})



class ProductDetailView(TemplateView):
    template_name = 'home/detail.html'
    def get(self,request,pk):
        product=Product.objects.filter(pk=pk)[0]
        form=AddToCartForm()
        return render(request,self.template_name,{'product':product,'form':form})
    def post(self,request,pk):
        form=AddToCartForm(request.POST)
        if form.is_valid():
            quantity=form.cleaned_data['quantity']
            user=request.user
            product=Product.objects.filter(pk=pk)[0]
            cart=CartDetails(cuser=user,cproduct=product,quantity=quantity)
            if cart:
                cart.save()
                text="Successfully added to cart"
            else:
                text="Failed Try again to add"
        form=AddToCartForm()
        return render(request,self.template_name,{'product':product,'form':form,'text':text})


def delete_product(request,pk):
    if pk:
        CartDetails.objects.filter(pk=pk).delete()
        cartProducts=CartDetails.objects.filter(cuser=request.user)
        total=0
        for line in cartProducts:total+=line.quantity*line.cproduct.price
        return render(request,'home/cart.html',{'cartProducts':cartProducts,'total':total})
