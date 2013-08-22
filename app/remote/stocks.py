__author__ = 'mriegel'

from datetime import datetime

STOCK_EXCHANGES = {
    'BA': {
        'name': 'Buenos Aires'
    }
}


remote = {
    'urls': {
        'de': 'http://de.finance.yahoo.com/d/quotes.csv?',
        'default': 'http://finance.yahoo.com/d/quotes.csv?',
        'de': 'http://de.finance.yahoo.com/d/quotes.csv?',
        'de': 'http://de.finance.yahoo.com/d/quotes.csv?',
    },
    'options': {
        'currency': 'c4',
        'commission': 'c3',
        'dividend': 'd',
        'dividend_share': 'd0',
        'last_trade_date': 'd1',
        'trade_date': 'd2',
        'days_low': 'g0',
        'holdings_gain_percent': 'g1',
        'annualized_gain': 'g3',
        'holdings_gain': 'g4',
        'holdings_gain_percent_realtime': 'g5',
        'holdings_gain_realtime': 'g6',
        'days_high': 'h0',
        'market_capitalization': 'j1',
        'market_capitalization_realtime': 'j3',
        'ebitda': 'j4',
        'last_trade_price': 'l1',
        'high_limit': 'l2',
        'low_limit': 'l3',
        'name': 'n0',
        'shares_owned': 's1',
        'short_ratio': 's7',
        'last_trade_time': 't1',
        'volume': 'v0',
        'stock_exchange': 'x0',
    },
    
}


class StockStorageClient():

    remote_url = ''

    def request(self, options=(), start=datetime(), end=datetime()):

        pass

    def call(self, url):
        pass

    def translate_options(self, options=()):
        pass

    pass