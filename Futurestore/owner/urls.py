from django.urls import path
from owner import views

urlpatterns=[path("index",views.AdminDashBoardView.as_view(),name="dashboard"),
             path("orders",views.NewOrdersView.as_view(),name="new-orders")]