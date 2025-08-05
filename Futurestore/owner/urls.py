from django.urls import path
from owner import views

urlpatterns=[path("index",views.AdminDashBoardView.as_view(),name="dashboard"),
             path("orders/latest",views.OrdersListView.as_view(),name="new-orders"),
             path("order/details/<int:id>",views.OrderDetailView.as_view(),name="order-details"),]