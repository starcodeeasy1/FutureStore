from django.urls import path
from owner import views

urlpatterns=[path("index",views.AdminDashBoardView.as_view(),name="dashboard")]