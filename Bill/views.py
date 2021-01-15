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
            bill = sale.bill_number.lstrip("kly-")
            billnumber = "kly-" + str(int(bill) + 1)
        else:
            billnumber = 'kly-1000'
        form = SalesForm(initial={'bill_number': billnumber})
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            billnumber = form.cleaned_data.get("bill_number")
            return redirect("billing", pk=billnumber)


class Order(TemplateView):
    model = OrderModel
    template_name = "billing.html"
    context = {}

    def get(self, request, *args, **kwargs):
        order = OrderModel.objects.filter(bill_number=kwargs["pk"])
        form = OrderForm(initial={"bill_number": kwargs["pk"]})
        self.context['orders'] = order
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):

        post = request.POST.copy()
        qty = post['quantity']
        pname = post['product_name']
        s_price = PurchaseModel.objects.get(product_name__product_name=pname).selling_price
        price = int(qty) * int(s_price)
        post['price'] = price

        form = OrderForm(post)
        if form.is_valid():
            form.save()
            billnumber = form.cleaned_data.get('bill_number')
            return redirect("billing", pk=billnumber)
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class DeleteOrder(TemplateView):
    def get(self, request, *args, **kwargs):
        billnumber = kwargs["pl"]
        OrderModel.objects.get(id=kwargs["pk"]).delete()
        return redirect("billing", pk=billnumber)


class Saless(TemplateView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        billno = data.get('billno')
        amount = data.get('total')
        SalesModel.objects.filter(bill_number=billno).update(bill_total=amount)
        return redirect("billing", pk=billno)
