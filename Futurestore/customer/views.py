from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,DetailView,UpdateView
from customer import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from owner.models import Product,Cart,Order
from django.contrib.auth import authenticate,login
#REGISTRATION VIEW
class RegistrationView(CreateView):
    model=User
    form_class=forms.RegistrationForm
    template_name="registration.html"
    success_url=reverse_lazy("login")
    
    def form_valid(self, form):
        messages.success(self.request,"your account has been created")
        return super().form_valid(form)

#LOGIN VIEW
class LoginView(FormView):
    template_name="login.html"
    form_class=forms.LoginForm
    # def get(self,request,*args,**kwargs):
    #     form=forms.LoginForm()
    #     return render(request,"login.html",{"form":form})
    def post(self, request, *args, **kwargs):
        form=forms.LoginForm(request.POST,files=request.FILES)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,"logged in successfully")
                if request.user.is_superuser:
                    return redirect("dashboard")
                else:
                    return redirect("home")
        else:
            return render(request,"login.html",{"form":form})
#INDEX VIEW(VIEW FOR HOME PAGE)
class HomeView(TemplateView):
    template_name="home.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # context["category"]=Category.objects.all()
        all_products=Product.objects.all()
        context["products"]=all_products
        return context
#VIEW FOR TAKING DETAILS OF A PRODUCT
class PoductDetailView(DetailView):
    model=Product
    template_name="product-detail.html"
    context_object_data="product"
    pk_url_kwarg="id"
#ADD TO CART VIEW
class AddToCart(FormView):
    template_name="add-to-cart.html"
    form_class=forms.CartForm
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        product=Product.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.CartForm,"product":product})
    def post(self, request, *args, **kwargs):
        id=kwargs.get("id")
        product=Product.objects.get(id=id)
        user=request.user
        form=forms.CartForm(request.POST)  #quantity=request.POST.get("quantity") instead of taking from form,can take like this
        if form.is_valid():
            Cart.objects.create(**form.cleaned_data,user=user,product=product)
            messages.success(request,"your item has been added to cart")
            return redirect("home")
#VIEW FOR LISTING ITEMS IN CART
class MyCartView(ListView):
    model=Cart
    template_name="cart-list.html"
    context_object_name="carts"
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")

#VIEW FOR ORDERING A PRODUCT OR AN ITEM
class PlaceOrderView(FormView):
    template_name="place-order.html"
    form_class=forms.OrderForm
    def post(self, request, *args, **kwargs):
        cart_id=kwargs.get("cid")
        product_id=kwargs.get("pid")
        cart=Cart.objects.get(id=cart_id)
        product=Product.objects.get(id=product_id)
        user=request.user
        # form=forms.OrderForm(request.POST)
        # if form.is_valid():
        #    return Order.objects.create(**form.cleaned_data,product=product,user=user)
        delivery_address=request.POST.get("delivery_address")
        Order.objects.create(product=product,user=user,delivery_address=delivery_address)
        cart.status="order-placed"
        cart.save()
        messages.success(request,"Order Placed")
        return redirect("home")
#VIEW FOR REMOVING A PRODUCT FROM CART)(UPDATING CART)
# class CartUpdateView(UpdateView):
#     template_name="cart-update.html"
#     def post(self, request, *args, **kwargs):
#         cart_id=kwargs.get("cid")
#         cart=Cart.objects.get(id=cart_id)
#         product_id=kwargs.get("pid")
#         product=Product.Objects.get(id=product_id)
#         cart.status="cancelled"
#         cart.save()
#         return redirect("home")


    

    



 