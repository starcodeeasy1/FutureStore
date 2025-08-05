from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from owner.models import Order
from django.contrib import messages
from owner.forms import OrderUpdateForm
#ADMIN DASHBOARD VIEW
class AdminDashBoardView(TemplateView):
    template_name="owner/dashboard.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["count"]=Order.objects.filter(status="order-placed").count()
        messages.success(self.request,"logged in successfully")
        return context
#TO LIST ALL NEW ORDERS
class OrdersListView(ListView):
    model=Order
    template_name="owner/order-list.html"
    context_object_name="orders"
    def get_queryset(self):
        return Order.objects.filter(status="order-placed").order_by("-created_date")
#VIEW FOR GETTING DETAILED SUMMERY OF ORDER
class OrderDetailView(DetailView):
    model=Order
    template_name="owner/order-details.html"
    context_object_name="order"
    pk_url_kwarg="id"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["form"]=OrderUpdateForm()
        return context


    