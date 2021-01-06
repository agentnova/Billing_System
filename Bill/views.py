from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Bill.models import ProductModel, SalesModel, PurchaseModel, OrderModel
from Bill.forms import ProductForm, Purchaseform, SalesForm, OrderForm


class product(TemplateView):
    model = ProductModel
    template_name = "product.html"
    context = {}
    context_object_name = "products"

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        products = self.model.objects.all()
        self.context["form"] = form
        self.context["products"] = products
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")


class EditProduct(TemplateView):
    model = ProductModel
    template_name = "product.html"
    context = {}
    context_object_name = "products"

    def get(self, request, *args, **kwargs):
        product = self.model.objects.get(id=kwargs["pk"])
        form = ProductForm(instance=product)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        product = self.model.objects.get(id=kwargs["pk"])
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("products")


class DeleteProduct(TemplateView):
    def get(self, request, *args, **kwargs):
        ProductModel.objects.get(id=kwargs["pk"]).delete()
        return redirect("products")


class Purchase(TemplateView):
    model = PurchaseModel
    template_name = "purchase.html"
    context = {}
    context_object_name = "purchases"

    def get(self, request, *args, **kwargs):
        purchases = self.model.objects.all()
        form = Purchaseform()
        self.context["form"] = form
        self.context["purchases"] = purchases
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = Purchaseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchases")


class EditPurchase(TemplateView):
    model = PurchaseModel
    template_name = "purchase.html"
    context = {}
    context_object_name = "purchases"

    def get(self, request, *args, **kwargs):
        purchase = self.model.objects.get(id=kwargs['pk'])
        form = Purchaseform(instance=purchase)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        purchase = self.model.objects.get(id=kwargs['pk'])
        form = Purchaseform(instance=purchase, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchases")


class DeletePurchase(TemplateView):
    def get(self, request, *args, **kwargs):
        PurchaseModel.objects.get(id=kwargs["pk"]).delete()
        return redirect("purchases")


class Sales(TemplateView):
    model = SalesModel
    context = {}
    template_name = "sales.html"

    def get(self, request, *args, **kwargs):

        sale = self.model.objects.all().last()
        if sale:
            print(sale.bill_number)
            bill = sale.bill_number.lstrip("kly-")
            print(bill)
            billnumber = "kly-" + str(int(bill) + 1)


        else:
            billnumber = 'kly-1000'
        form = SalesForm(initial={'bill_number': billnumber})
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = SalesForm(request.POST)
        if form.is_valid():
            billnumber = form.cleaned_data.get("bill_number")
            form.save()
            return redirect("billing", pk=billnumber)


class Order(TemplateView):
    model = OrderModel
    template_name = "billing.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = OrderForm(initial={"bill_number": kwargs["pk"]})
        self.context["form"] = form
        return render(request, self.template_name, self.context)