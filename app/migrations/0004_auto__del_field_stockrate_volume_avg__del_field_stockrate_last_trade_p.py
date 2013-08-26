# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'StockRate.volume_avg'
        db.delete_column(u'app_stockrate', 'volume_avg')

        # Deleting field 'StockRate.last_trade_price'
        db.delete_column(u'app_stockrate', 'last_trade_price')

        # Deleting field 'StockRate.high_limit_price'
        db.delete_column(u'app_stockrate', 'high_limit_price')

        # Deleting field 'StockRate.low_limit_price'
        db.delete_column(u'app_stockrate', 'low_limit_price')

        # Adding field 'StockRate.open'
        db.add_column(u'app_stockrate', 'open',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'StockRate.close'
        db.add_column(u'app_stockrate', 'close',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'StockRate.high'
        db.add_column(u'app_stockrate', 'high',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'StockRate.low'
        db.add_column(u'app_stockrate', 'low',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'StockRate.volume_avg'
        db.add_column(u'app_stockrate', 'volume_avg',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'StockRate.last_trade_price'
        raise RuntimeError("Cannot reverse this migration. 'StockRate.last_trade_price' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'StockRate.last_trade_price'
        db.add_column(u'app_stockrate', 'last_trade_price',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'StockRate.high_limit_price'
        raise RuntimeError("Cannot reverse this migration. 'StockRate.high_limit_price' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'StockRate.high_limit_price'
        db.add_column(u'app_stockrate', 'high_limit_price',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'StockRate.low_limit_price'
        raise RuntimeError("Cannot reverse this migration. 'StockRate.low_limit_price' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'StockRate.low_limit_price'
        db.add_column(u'app_stockrate', 'low_limit_price',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)

        # Deleting field 'StockRate.open'
        db.delete_column(u'app_stockrate', 'open')

        # Deleting field 'StockRate.close'
        db.delete_column(u'app_stockrate', 'close')

        # Deleting field 'StockRate.high'
        db.delete_column(u'app_stockrate', 'high')

        # Deleting field 'StockRate.low'
        db.delete_column(u'app_stockrate', 'low')


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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 26, 0, 0)', 'db_index': 'True'}),
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
            'enabled_stock_exchanges': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'enabled_stock_exchanges'", 'symmetrical': 'False', 'to': u"orm['app.StockExchange']"}),
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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 26, 0, 0)'}),
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
            'suffix_yahoo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'symbol_finanzennet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'symbol_yahoo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'app.stockrate': {
            'Meta': {'object_name': 'StockRate'},
            'close': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 26, 0, 0)', 'db_index': 'True'}),
            'high': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.FloatField', [], {}),
            'open': ('django.db.models.fields.FloatField', [], {}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Stock']"}),
            'stock_exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.StockExchange']"}),
            'volume': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.stocksplit': {
            'Meta': {'object_name': 'StockSplit'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 26, 0, 0)', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_shares_after': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_shares_before': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Stock']"}),
            'stock_exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.StockExchange']"})
        }
    }

    complete_apps = ['app']