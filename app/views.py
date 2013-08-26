__author__ = 'mriegel'

from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from app.helper.string import is_isin, is_wkn
from pprint import pprint


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
def stock_add(request):
    from app.remote.stocks import StockHistoryClient
    from app.forms import StockWizardForm
    from app.models import Company, Stock

    if request.method == "POST":
        form = StockWizardForm(request.POST)
        pprint(form.is_valid())
        if form.is_valid():
            # save
            company = Company()
            company.name = form.cleaned_data['company_name']
            company.country = form.cleaned_data['company_country']
            company.save()

            stock = Stock()
            stock.company = company
            stock.name = form.cleaned_data['name']
            stock.wkn = form.cleaned_data['wkn']
            stock.isin = form.cleaned_data['isin']
            stock.symbol = form.cleaned_data['symbol']
            stock.type = form.cleaned_data['type']
            stock.default_stock_exchange = form.cleaned_data['default_stock_exchange']
            stock.save()

            return HttpResponseRedirect(reverse('stock', args=(stock.symbol,)))
        else:
            pprint(form.errors)
    else:
        data = None
        if 'wkn_or_isin' in request.GET:
            shc = StockHistoryClient()
            data = shc.get_basics_by_wkn_or_isin(wkn_or_isin=request.GET['wkn_or_isin'])

            data['company_country'] = data['country']
            data['company_name'] = data['name']

        form = StockWizardForm(initial=data)

    return render_to_response(
        'stock_wizard_add.html',
        {
            'form': form
        },
        context_instance=RequestContext(request)
    )


@login_required()
def stock_search(request):

    if 'q' not in request.GET:
        return HttpResponseRedirect(reverse('dashboard'))

    from app.models import Stock

    query = request.GET['q']

    if is_isin(query) or is_wkn(query):
        try:
            if is_isin(query):
                stock = Stock.objects.get(isin=query)
            else:
                stock = Stock.objects.get(wkn=query)
            return HttpResponseRedirect(reverse('stock', args=(stock.symbol,)))
        except Stock.DoesNotExist:
            qs = "wkn_or_isin=%s" % query
            print '?'.join((reverse('add_stock'), qs))
            return HttpResponseRedirect('?'.join((reverse('add_stock'), qs)))


    return render_to_response(
        'stock_search_result.html',
        {
            #'stock': stock
        },
        context_instance=RequestContext(request)
    )


@login_required()
def stock_rates_json(request, symbol):
    from models import Stock, StockRate
    import json

    stock = Stock.objects.get(symbol=symbol)
    stock_exchange = stock.default_stock_exchange

    if not stock:
        return Http404()

    rates = StockRate.objects.filter(stock=stock, stock_exchange=stock_exchange).order_by('date')

    data = []
    for rate in rates:
        sub_json = {
            'date': int(rate.date.strftime('%s')) * 1000,
            'open': rate.open,
            'close': rate.close,
            'high': rate.high,
            'low': rate.low,
            'volume': rate.volume,
        }
        data.append(sub_json)

    response = {
        'data': data,
        'name': "%s at %s" % (stock.symbol, stock.default_stock_exchange)
    }

    return HttpResponse(json.dumps(response), content_type="application/json")


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
            sr = StockRate.objects.get(stock=stock, date=result['date'], stock_exchange=stock_exchange)
        except StockRate.DoesNotExist:
            sr = StockRate()
            sr.stock = stock
            sr.stock_exchange = stock_exchange
            sr.date = result['date']

        sr.volume = result['volume']
        sr.close = result['close']
        sr.high = result['high']
        sr.low = result['low']
        sr.open = result['open']
        sr.save()

    return HttpResponseRedirect(reverse('stock', args=(stock.symbol,)))
