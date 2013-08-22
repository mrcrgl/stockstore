__author__ = 'riegel'

from django.core.management.base import BaseCommand, CommandError
from app.models import Share, DailyShareRate
from app.remote.stocks import StockStorageClient
from pprint import pprint


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = StockStorageClient()
        shares = Share.objects.filter()

        for share in shares:
            self.stdout.write("Proceed Share %s" % share.name)
            result = client.request(
                options=[
                    'ask',
                    'currency',
                    'commission',
                    'dividend',
                    'dividend_share',
                    'last_trade_date',
                    'trade_date',
                    'days_low',
                    'holdings_gain_percent',
                    'annualized_gain',
                    'holdings_gain',
                    'holdings_gain_percent_realtime',
                    'holdings_gain_realtime',
                    'days_high',
                    'market_capitalization',  # Mkt Cap.
                    'market_capitalization_realtime',
                    'ebitda',  # This is the share value?
                    'last_trade_price',
                    'high_limit',
                    'low_limit',
                    'name',
                    'shares_owned',
                    'short_ratio',
                    'last_trade_time',
                    'volume',
                    'stock_exchange',
                ],
                symbol=share.symbol
            )

            pprint(result)

            #raise CommandError('Test Error')