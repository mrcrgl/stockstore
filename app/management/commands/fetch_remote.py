__author__ = 'riegel'

from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.remote.stocks import StockStorageClient
from pprint import pprint


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = StockStorageClient()
        stocks = Stock.objects.filter()

        from app.models import StockRate, StockExchange

        for stock in stocks:
            self.stdout.write("Proceed Stock %s" % stock.name)
            result = client.request(
                options=[
                    #'ask',
                    'currency',
                    #'commission',
                    'dividend',
                    'dividend_share',
                    'last_trade_date',
                    'trade_date',
                    'days_low',
                    #'holdings_gain_percent',
                    'annualized_gain',
                    #'holdings_gain',
                    #'holdings_gain_percent_realtime',
                    #'holdings_gain_realtime',
                    'days_high',
                    'market_capitalization',  # Mkt Cap.
                    #'market_capitalization_realtime',
                    #'ebitda',  # This is the share value?
                    'last_trade_price',
                    'high_limit',
                    'low_limit',
                    'open',
                    'name',
                    #'shares_owned',
                    'short_ratio',
                    #'last_trade_time',
                    'volume',
                    'stock_exchange',
                ],
                symbol=stock.symbol
            )

            """
            TODO
            Check if stock has changed, if its -> change it and notify about it
            Add the new rates
            """

            """
            stock = models.ForeignKey(Stock, verbose_name="Share", db_index=True)
            date = models.DateField(default=datetime.now(), verbose_name="Close date", db_index=True)
            stock_exchange = models.ForeignKey(StockExchange, verbose_name="Stock Exchange")
            volume = models.IntegerField(verbose_name="Volume of trades")
            volume_avg = models.IntegerField(verbose_name="Avg volume of trades")
            last_trade_price = models.FloatField(verbose_name="Price: Close")
            high_limit_price = models.FloatField(verbose_name="Price: High")
            low_limit_price = models.FloatField(verbose_name="Price: Low")
            """

            exchange = StockExchange.objects.get(symbol_yahoo=result['stock_exchange'])

            if not exchange:
                raise NotImplementedError("Stock exchange with symbol '%s' not found." % result.stock_exchange)

            try:
                stock_rate = StockRate.objects.get(
                    stock=stock,
                    date=result['last_trade_date'],
                    stock_exchange=exchange
                )
            except StockRate.DoesNotExist:
                stock_rate = StockRate()

            stock_rate.close = result['last_trade_price']
            stock_rate.high = result['days_high']
            stock_rate.low = result['days_low']
            stock_rate.open = result['open']
            stock_rate.volume = result['volume']
            stock_rate.stock = stock
            stock_rate.date = result['last_trade_date']
            stock_rate.stock_exchange = exchange
            stock_rate.save()

            #pprint(result)
            #if stock.num_shares != result['']