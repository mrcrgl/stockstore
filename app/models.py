__author__ = 'mriegel'

from django.db import models
from datetime import datetime
from django_countries import CountryField


class Currency(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name")
    sign = models.CharField(max_length=5, verbose_name="Sign")
    symbol = models.CharField(max_length=10, verbose_name="Symbol")
    base_rate = models.FloatField(verbose_name="Base Rate to EUR")

    def __unicode__(self):
        return "%s (%s, %s)" % (self.name, self.sign, self.symbol)


class CurrencyExchangeRate(models.Model):
    date = models.DateField(default=datetime.now(), db_index=True)
    currency = models.ForeignKey(Currency, db_index=True, verbose_name="Currency")
    to_currency = models.ForeignKey(Currency, verbose_name="To Currency", related_name="to_currency", default=1)
    rate = models.FloatField()


class StockExchange(models.Model):
    currency = models.ForeignKey(Currency, verbose_name="Currency")
    name = models.CharField(max_length=30, verbose_name="Name")
    symbol_yahoo = models.CharField(max_length=30, verbose_name="Symbol (Yahoo)", blank=True)
    suffix_yahoo = models.CharField(max_length=30, verbose_name="Suffix (Yahoo)", blank=True)
    symbol_finanzennet = models.CharField(max_length=30, verbose_name="Symbol (finanzen.net)", blank=True)
    country = CountryField(verbose_name="Country", default="DE")

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name")
    country = CountryField(verbose_name="Country", default="DE")

    def __unicode__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name")
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child_sector_set',
    )

    def __unicode__(self):
        return self.name


class Stock(models.Model):
    TYPE_SHARE = 'share'
    TYPE_RESOURCE = 'resource'  # Rohstoff
    TYPE_FOND = 'fond'
    TYPE_BOND = 'bond'

    TYPE_CHOICES = (
        (TYPE_SHARE, 'Share'),
        (TYPE_RESOURCE, 'Resource'),
        (TYPE_FOND, 'Fond'),
        (TYPE_BOND, 'Bond'),
    )

    name = models.CharField(max_length=60, verbose_name="Name")
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default=TYPE_SHARE, verbose_name="Type")
    sector = models.ForeignKey(Sector, db_index=True, verbose_name="Sector", null=True, blank=True)
    company = models.ForeignKey(Company, verbose_name="Company", db_index=True, default="DE")
    currency = models.ForeignKey(Currency, verbose_name="Currency", null=True, blank=True)
    default_stock_exchange = models.ForeignKey(
        StockExchange,
        verbose_name="Default Stock Exchange",
        null=True,
        blank=True
    )
    enabled_stock_exchanges = models.ManyToManyField(
        StockExchange,
        verbose_name="Enabled stock exchanges",
        related_name="enabled_stock_exchanges"
    )
    wkn = models.CharField(max_length=6, verbose_name="WKN", db_index=True, null=True, blank=True)
    isin = models.CharField(max_length=12, verbose_name="ISIN", db_index=True, null=True, blank=True)
    symbol = models.CharField(max_length=30, verbose_name="Symbol", db_index=True, null=True, blank=True)
    num_shares = models.IntegerField(verbose_name="Number of Shares", null=True, blank=True)

    def __unicode__(self):
        return self.name


class StockDividend(models.Model):
    stock = models.ForeignKey(Stock, db_index=True, verbose_name="Stock")
    date = models.DateField(default=datetime.now(), verbose_name="Date")
    value = models.FloatField(verbose_name="Value")


class StockRate(models.Model):
    stock = models.ForeignKey(Stock, verbose_name="Share", db_index=True)
    date = models.DateField(default=datetime.now(), verbose_name="Close date", db_index=True)
    stock_exchange = models.ForeignKey(StockExchange, verbose_name="Stock Exchange")
    volume = models.IntegerField(verbose_name="Volume of trades")
    open = models.FloatField(verbose_name="Price: Low")
    close = models.FloatField(verbose_name="Price: Close")
    high = models.FloatField(verbose_name="Price: High")
    low = models.FloatField(verbose_name="Price: Low")


class StockSplit(models.Model):
    stock = models.ForeignKey(Stock, verbose_name="Share", db_index=True)
    date = models.DateField(default=datetime.now(), verbose_name="Date", db_index=True)
    stock_exchange = models.ForeignKey(StockExchange, verbose_name="Stock Exchange")
    num_shares_before = models.IntegerField(verbose_name="Number of Shares before", null=True, blank=True)
    num_shares_after = models.IntegerField(verbose_name="Number of Shares after", null=True, blank=True)
    #country = models.ForeignKey(Country, verbose_name="Country")