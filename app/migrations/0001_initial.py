# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table(u'app_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('sign', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('base_rate', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['Currency'])

        # Adding model 'CurrencyExchangeRate'
        db.create_table(u'app_currencyexchangerate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 25, 0, 0), db_index=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Currency'])),
            ('to_currency', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='to_currency', to=orm['app.Currency'])),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['CurrencyExchangeRate'])

        # Adding model 'StockExchange'
        db.create_table(u'app_stockexchange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Currency'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('symbol_yahoo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('symbol_finanzennet', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django_countries.fields.CountryField')(default='DE', max_length=2)),
        ))
        db.send_create_signal(u'app', ['StockExchange'])

        # Adding model 'Company'
        db.create_table(u'app_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('country', self.gf('django_countries.fields.CountryField')(default='DE', max_length=2)),
        ))
        db.send_create_signal(u'app', ['Company'])

        # Adding model 'Sector'
        db.create_table(u'app_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_sector_set', null=True, to=orm['app.Sector'])),
        ))
        db.send_create_signal(u'app', ['Sector'])

        # Adding model 'Stock'
        db.create_table(u'app_stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('type', self.gf('django.db.models.fields.CharField')(default='share', max_length=8)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Sector'], null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(default='DE', to=orm['app.Company'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Currency'], null=True, blank=True)),
            ('default_stock_exchange', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.StockExchange'], null=True, blank=True)),
            ('wkn', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=6, null=True, blank=True)),
            ('isin', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=12, null=True, blank=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=30, null=True, blank=True)),
            ('num_shares', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Stock'])

        # Adding model 'StockDividend'
        db.create_table(u'app_stockdividend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Stock'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 25, 0, 0))),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['StockDividend'])

        # Adding model 'StockRate'
        db.create_table(u'app_stockrate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Stock'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 25, 0, 0), db_index=True)),
            ('stock_exchange', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.StockExchange'])),
            ('volume', self.gf('django.db.models.fields.IntegerField')()),
            ('volume_avg', self.gf('django.db.models.fields.IntegerField')()),
            ('last_trade_price', self.gf('django.db.models.fields.FloatField')()),
            ('high_limit_price', self.gf('django.db.models.fields.FloatField')()),
            ('low_limit_price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['StockRate'])

        # Adding model 'StockSplit'
        db.create_table(u'app_stocksplit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Stock'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 25, 0, 0), db_index=True)),
            ('stock_exchange', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.StockExchange'])),
            ('num_shares_before', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_shares_after', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['StockSplit'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table(u'app_currency')

        # Deleting model 'CurrencyExchangeRate'
        db.delete_table(u'app_currencyexchangerate')

        # Deleting model 'StockExchange'
        db.delete_table(u'app_stockexchange')

        # Deleting model 'Company'
        db.delete_table(u'app_company')

        # Deleting model 'Sector'
        db.delete_table(u'app_sector')

        # Deleting model 'Stock'
        db.delete_table(u'app_stock')

        # Deleting model 'StockDividend'
        db.delete_table(u'app_stockdividend')

        # Deleting model 'StockRate'
        db.delete_table(u'app_stockrate')

        # Deleting model 'StockSplit'
        db.delete_table(u'app_stocksplit')


    models = {
        u'app.company': {
            'Meta': {'object_name': 'Company'},
            'country': ('django_countries.fields.CountryField', [], {'default': "'DE'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'app.currency': {
            'Meta': {'object_name': 'Currency'},
            'base_rate': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'app.currencyexchangerate': {
            'Meta': {'object_name': 'CurrencyExchangeRate'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 25, 0, 0)', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {}),
            'to_currency': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'to_currency'", 'to': u"orm['app.Currency']"})
        },
        u'app.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_sector_set'", 'null': 'True', 'to': u"orm['app.Sector']"})
        },
        u'app.stock': {
            'Meta': {'object_name': 'Stock'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'default': "'DE'", 'to': u"orm['app.Company']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Currency']", 'null': 'True', 'blank': 'True'}),
            'default_stock_exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.StockExchange']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'num_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Sector']", 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'share'", 'max_length': '8'}),
            'wkn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        u'app.stockdividend': {
            'Meta': {'object_name': 'StockDividend'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Stock']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.stockexchange': {
            'Meta': {'object_name': 'StockExchange'},
            'country': ('django_countries.fields.CountryField', [], {'default': "'DE'", 'max_length': '2'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'symbol_finanzennet': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'symbol_yahoo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.stockrate': {
            'Meta': {'object_name': 'StockRate'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 25, 0, 0)', 'db_index': 'True'}),
            'high_limit_price': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_trade_price': ('django.db.models.fields.FloatField', [], {}),
            'low_limit_price': ('django.db.models.fields.FloatField', [], {}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Stock']"}),
            'stock_exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.StockExchange']"}),
            'volume': ('django.db.models.fields.IntegerField', [], {}),
            'volume_avg': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.stocksplit': {
            'Meta': {'object_name': 'StockSplit'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 25, 0, 0)', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_shares_after': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_shares_before': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Stock']"}),
            'stock_exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.StockExchange']"})
        }
    }

    complete_apps = ['app']