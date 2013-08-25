__author__ = 'mriegel'

from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


@login_required()
def dashboard(request):
    from models import Stock

    stocks = Stock.objects.all()

    return render_to_response(
        'dashboard.html',
        {
            'stocks': stocks
        },
        context_instance=RequestContext(request)
    )


@login_required()
def stock(request, symbol):
    from models import Stock

    stock = Stock.objects.get(symbol=symbol)

    if not stock:
        return Http404()

    return render_to_response(
        'stock.html',
        {
            'stock': stock
        },
        context_instance=RequestContext(request)
    )


@login_required()
def stock_fetch_history(request, symbol):
    from models import Stock, StockRate
    from app.remote.stocks import StockHistoryClient

    stock = Stock.objects.get(symbol=symbol)
    stock_exchange = stock.default_stock_exchange

    if not stock:
        return Http404()

    shc = StockHistoryClient()

    results = shc.request(stock, stock_exchange)

    for result in results:
        try:
            sr = StockRate.objects.get(stock=stock, date=result['last_trade_date'], stock_exchange=stock_exchange)
        except StockRate.DoesNotExist:
            sr = StockRate()
            sr.stock = stock
            sr.stock_exchange = stock_exchange
            sr.date = result['last_trade_date']

        sr.volume = result['volume']
        sr.volume_avg = result['volume']
        sr.last_trade_price = result['last_trade_price']
        sr.high_limit_price = result['day_high']
        sr.low_limit_price = result['day_low']
        sr.save()

    return HttpResponseRedirect(reverse('stock', args=(stock.symbol,)))
