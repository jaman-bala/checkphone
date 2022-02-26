from django import forms
from .models import Base


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = ('phone_models', 'imei', 'organization', 'num', 'erp')
        widgets = {

            "phone_models": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Модель телефона"
                       }),
            "imei": forms.NumberInput(
                attrs={"class": "form-control",
                       "placeholder": "ИМЕЙ КОД"
                       }),
            "organization": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Инициатор"
                       }),
            "num": forms.NumberInput(
                attrs={"class": "form-control",
                       "placeholder": "Номер инициатора"
                       }),
            "erp": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Номер ЕРП"
                       }),
        }
