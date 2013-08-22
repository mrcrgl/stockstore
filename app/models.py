__author__ = 'mriegel'

from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name")
    sign = models.CharField(max_length=30, verbose_name="Sign")
    base_rate = models.FloatField(verbose_name="Base Rate")


class Company(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name")


class Share(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name")
    symbol = models.CharField(max_length=30, verbose_name="WKN")
    company = models.ForeignKey(Company, verbose_name="Company")
    currency = models.ForeignKey(Currency, verbose_name="Currency")
    dividend = models.FloatField(verbose_name="Dividend")
    num_shares = models.IntegerField(verbose_name="Number of Shares")


class DailyShareRate(models.Model):
    share = models.ForeignKey(Share, verbose_name="Share")
    date = models.CharField(max_length=60, verbose_name="Close date")
    volume = models.IntegerField(verbose_name="Volume of trades")
    volume_avg = models.IntegerField(verbose_name="Avg volume of trades")
    last_trade_price = models.FloatField(verbose_name="Price: Close")
    high_limit_price = models.FloatField(verbose_name="Price: High")
    low_limit_price = models.FloatField(verbose_name="Price: Low")


#class StockExchange(models.Model):
    #name = models.CharField(max_length=30, verbose_name="Exchange name")
    #country = models.ForeignKey(Country, verbose_name="Country")