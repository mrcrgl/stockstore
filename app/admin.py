__author__ = 'mriegel'

from django.contrib import admin
from models import *


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sign', 'base_rate', )
    pass


class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate', )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    pass


class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    pass


class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', )
    pass


class StockRateAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'last_trade_price', )
    pass


class StockDividendAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'value', )
    pass


class StockExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    pass


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyExchangeRate, CurrencyExchangeRateAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockRate, StockRateAdmin)
admin.site.register(StockDividend, StockDividendAdmin)
admin.site.register(StockExchange, StockExchangeAdmin)