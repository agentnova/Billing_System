from Bill.models import ProductModel, SalesModel, PurchaseModel, OrderModel
from django.forms import ModelForm
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
        widgets = {
            "product_name": forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        productname = cleaned_data.get("product_name")
        product = ProductModel.objects.filter(product_name=productname)
        if product:
            msg = "product already exist"
            self.add_error('product_name', msg)


class Purchaseform(ModelForm):
    class Meta:
        model = PurchaseModel
        fields = ["product_name", "quantity", "buying_price", "selling_price"]
        widgets = {
            "product_name": forms.Select(attrs={'class': 'custom-select'}),
            "quantity": forms.NumberInput(attrs={'class': 'form-control'}),
            "buying_price": forms.NumberInput(attrs={'class': 'form-control'}),
            "selling_price": forms.NumberInput(attrs={'class': 'form-control'})
        }


class SalesForm(ModelForm):
    class Meta:
        model = SalesModel
        fields = ['bill_number', 'customer_name', 'phone']


class OrderForm(ModelForm):
    bill_number = forms.CharField()
    purchase = PurchaseModel.objects.all().values_list("product_name__product_name", flat=True).distinct()
    choice = [(name, name) for name in purchase]
    product_name = forms.ChoiceField(choices=choice, required=False, widget=forms.Select())

    class Meta:
        model = OrderModel
        fields = ['bill_number', 'product_name', 'quantity']
