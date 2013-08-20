__author__ = 'mriegel'

from django.contrib import admin
from models import Currency, Company, Share, DailyShareRate


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sign', 'base_rate', )
    pass


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    pass


class ShareAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', )
    pass


class DailyShareRateAdmin(admin.ModelAdmin):
    list_display = ('date', )
    pass


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Share, ShareAdmin)
admin.site.register(DailyShareRate, DailyShareRateAdmin)