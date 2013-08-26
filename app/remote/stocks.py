__author__ = 'mriegel'

from datetime import datetime
import urllib2
from pprint import pprint
from app.helper.string import clear_quotation_marks
from app.helper.integer import clear_float, clear_number
from app.helper.date import string_to_datetime
import re
import urllib
from datetime import datetime


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
    'open': 'o0',
    'name': 'n0',
    'shares_owned': 's1',
    'short_ratio': 's7',
    'last_trade_time': 't1',
    'volume': 'v0',
    'stock_exchange': 'x0',

}

FORMAT_STRING = [
    'annualized_gain',
    'currency',
    'holdings_gain_percent_realtime',
    'holdings_gain_percent',
    'name',
    'stock_exchange',
    'last_trade_date',
    'last_trade_time',
    'trade_date',
]

FORMAT_DATETIME = [
    'last_trade_date',
    'last_trade_time',
    'trade_date',
]

FORMAT_NUMBER = [
    'ebitda',
    'market_capitalization',
    'volume',
    'shares_owned',

]

FORMAT_FLOAT = [
    'ask',
    'days_high',
    'days_low',
    'open',
    'dividend',
    'dividend_share',
    'last_trade_price',
    'short_ratio',
    'holdings_gain',
    'high_limit',
    'low_limit',
    'commission',
    'annualized_gain',
]


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
        pprint(values)
        for option in options:
            temp = values.pop(0)

            if temp == 'N/A':
                pass  #pprint(option)

            if option in FORMAT_STRING:
                temp = clear_quotation_marks(temp)

            if option in FORMAT_NUMBER:
                temp = clear_number(temp)

            if option in FORMAT_FLOAT:
                temp = clear_float(temp)

            if option in FORMAT_DATETIME:
                temp = string_to_datetime(temp)

            #pprint(temp)
            return_object[option] = temp
            #pprint(clear_quotation_marks(return_object[option]))

        return return_object

    pass


class StockHistoryClient():

    fnet_host = 'www.finanzen.net'
    search_path = '/suchergebnis.asp?frmAktiensucheTextfeld=%s'
    history_path = '/kurse/kurse_historisch.asp'
    r_share_id = r'pkAktieNr=([0-9]+)'
    #r_historic_table = r'class="content"\>\<table\>(.*)\<\/table\>'
    r_historic_table = r'([0-9]{2})\.([0-9]{2}).([0-9]{4})\<\/td\>\<td\>([0-9,]+)\<\/td\>\<td\>([0-9,]+)\<\/td\>\<td\>([0-9,]+)\<\/td\>\<td\>([0-9,]+)\<\/td\>\<td\>([0-9\.]+)\<\/td\>'

    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.finanzen.net',
        'Referer': 'http://www.finanzen.net/kurse/kurse_historisch.asp',
    }

    def get_basics_by_wkn_or_isin(self, wkn_or_isin):
        url = self.search_path % wkn_or_isin
        response = self.call(url)
        # WKN: 850663 / ISIN: US1912161007
        matches = re.search(r'WKN: ([0-9A-Z]{6})', response, flags=0)
        wkn = matches.group(1)

        matches = re.search(r'ISIN: ([0-9A-Z]{12})', response, flags=0)
        isin = matches.group(1)
        country = isin[:2]

        matches = re.search(r'>([a-zA-Z_\- ]+) \[WKN', response, flags=0)
        name = matches.group(1).strip()

        type = None
        if "Aktie" in name:
            type = 'share'
            name = name.replace("Aktie", "").strip()

        return {
            'wkn': wkn,
            'isin': isin,
            'name': name,
            'country': country,
            'type': type
        }

    def request(self, stock, exchange):

        url = self.search_path % stock.wkn
        response = self.call(url)
        matches = re.search(self.r_share_id, response, flags=0)
        fnet_share_id = int(matches.group(1))
        now = datetime.now()

        params = urllib.urlencode({
            'dtTag1': 1,
            'dtMonat1': 1,
            'dtJahr1': 1990,
            'dtTag2': now.day,
            'dtMonat2': now.month,
            'dtJahr2': now.year,
            'strBoerse': exchange.symbol_finanzennet,
            'pkAktieNr': fnet_share_id,
            'strAktieWKN': stock.wkn,
            'strAktieISIN': stock.isin,
            'strAktieSymbol': stock.symbol,
            #'strAktieName': stock.name,
        })

        history_response = self.call(self.history_path, params)

        matches = re.findall(self.r_historic_table, history_response, flags=0)

        return_results = []
        for match in matches:
            day = match[0]
            month = match[1]
            year = match[2]
            open = clear_float(match[3].replace(',', '.'))
            close = clear_float(match[4].replace(',', '.'))
            high = clear_float(match[5].replace(',', '.'))
            low = clear_float(match[6].replace(',', '.'))
            volume = clear_number(match[7].replace('.', ''))

            res = {
                'date': string_to_datetime("%s/%s/%s" % (month, day, year)),
                'high': high,
                'low': low,
                'close': close,
                'open': open,
                'volume': volume,
            }
            #pprint(res)
            return_results.append(res)

        return return_results

    def call(self, url, data=None):
        import httplib

        method = "GET"

        if data is not None:
            method = "POST"

        conn = httplib.HTTPConnection(self.fnet_host, timeout=10)
        conn.request(method, url=url, body=data, headers=self.default_headers)
        response = conn.getresponse()
        location = response.getheader('location')

        if location:
            return self.call(location)

        return response.read()