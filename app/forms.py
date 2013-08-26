__author__ = 'riegel'

from django import forms
from django_countries.countries import COUNTRIES
from app.models import StockExchange, Stock


class StockWizardForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label="Name")
    company_name = forms.CharField(max_length=60, required=True, label="Company Name")
    company_country = forms.ChoiceField(choices=COUNTRIES, label="Company Country")
    wkn = forms.CharField(max_length=6, required=True, label="WKN")
    isin = forms.CharField(max_length=12, required=True, label="ISIN")
    symbol = forms.CharField(max_length=6, required=True, label="Symbol")
    type = forms.ChoiceField(choices=Stock.TYPE_CHOICES, required=True, label="Type")
    default_stock_exchange = forms.ModelChoiceField(queryset=StockExchange.objects.all().order_by('name'))
