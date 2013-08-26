__author__ = 'mriegel'

from django.contrib import admin
from models import *


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sign', 'base_rate', )
    pass


class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate', )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    list_filter = ('country',)
    pass


class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    pass


class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'sector', 'type', 'symbols', )

    def symbols(self, obj):
        return "%s / %s / %s" % (obj.symbol, obj.wkn, obj.isin)

    def country(self, obj):
        return obj.company.country

    symbols.short_description = "Symbol / WKN / ISIN"

    list_filter = ('type', 'sector',)


class StockRateAdmin(admin.ModelAdmin):
    list_display = ('stock', 'stock_exchange', 'date', 'close', )
    list_filter = ('stock', 'stock_exchange', )
    pass


class StockDividendAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'value', )
    list_filter = ('stock',)
    pass


class StockExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol_yahoo', 'symbol_finanzennet')
    pass


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyExchangeRate, CurrencyExchangeRateAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockRate, StockRateAdmin)
admin.site.register(StockDividend, StockDividendAdmin)
admin.site.register(StockExchange, StockExchangeAdmin)