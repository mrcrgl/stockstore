__author__ = 'mriegel'

from datetime import datetime
import urllib2
from pprint import pprint


STOCK_EXCHANGES = {
    'BA': {
        'name': 'Buenos Aires'
    }
}

REMOTE_URLS = {
    'de': 'http://de.finance.yahoo.com/d/quotes.csv?',
    'default': 'http://finance.yahoo.com/d/quotes.csv?',
}

REMOTE_OPTIONS = {
    'ask': 'a',
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

}


class StockStorageClient():
    def request(self, symbol, options=[]):
        options.sort()
        request_params = self.translate_options(options)
        url = self.build_url(request_params, symbol)
        response = self.call(url)
        return self.translate_response(
            response=response,
            options=options
        )

    def call(self, url):
        response = urllib2.urlopen(url)
        return response.read()

    def build_url(self, request_params, symbol, base_url='default'):
        return "%sf=%s&s=%s" % (REMOTE_URLS[base_url], request_params, symbol)
        pass

    def translate_options(self, options=[]):
        params = ''
        for option in options:
            if option not in REMOTE_OPTIONS:
                raise AttributeError("Undefined option: %s" % option)
            params += REMOTE_OPTIONS[option]

        return params

    def translate_response(self, options, response):
        values = response.split(',')
        return_object = {}
        #pprint(options)
        for option in options:
            return_object[option] = values.pop(0)

        return return_object

    pass