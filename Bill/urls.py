"""BillMaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Bill.views import product, EditProduct, DeleteProduct, Purchase, EditPurchase, DeletePurchase, Sales, Order, \
    DeleteOrder, Saless, ViewBills,DeleteBill

urlpatterns = [
    path('products/', product.as_view(), name="products"),
    path('editproduct/<int:pk>', EditProduct.as_view(), name="editproduct"),
    path('deleteproduct/<int:pk>', DeleteProduct.as_view(), name="deleteproduct"),
    path('purchases/', Purchase.as_view(), name="purchases"),
    path('editpurchase/<int:pk>', EditPurchase.as_view(), name="editpurchase"),
    path('deletepurchase/<int:pk>', DeletePurchase.as_view(), name="deletepurchase"),
    path('sales/', Sales.as_view(), name="sales"),
    path('billing/<str:pk>', Order.as_view(), name="billing"),
    path('deleteorder/<str:pk>/<str:pl>', DeleteOrder.as_view(), name="deleteorder"),
    path('saless/', Saless.as_view(), name="saless"),
    path('bills/', ViewBills.as_view(), name="bills"),
    path('deletebill/<int:pk>',DeleteBill.as_view(),name="deletebill")
]
