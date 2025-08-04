from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from owner.models import Order
#ADMIN DASHBOARD VIEW
class AdminDashBoardView(TemplateView):
    template_name="dashboard.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["count"]=Order.objects.filter(status="order-placed").count()
        return context
#TO LIST ALL NEW ORDERS
class NewOrdersView(ListView):
    model=Order
    template_name="order-list.html"
    context_object_name="orders"


    