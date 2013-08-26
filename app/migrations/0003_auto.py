# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field enabled_stock_exchanges on 'Stock'
        m2m_table_name = db.shorten_name(u'app_stock_enabled_stock_exchanges')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('stock', models.ForeignKey(orm[u'app.stock'], null=False)),
            ('stockexchange', models.ForeignKey(orm[u'app.stockexchange'], null=False))
        ))
        db.create_unique(m2m_table_name, ['stock_id', 'stockexchange_id'])


    def backwards(self, orm):
        # Removing M2M table for field enabled_stock_exchanges on 'Stock'
        db.delete_table(db.shorten_name(u'app_stock_enabled_stock_exchanges'))


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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 26, 0, 0)', 'db_index': 'True'}),
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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 26, 0, 0)', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_shares_after': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_shares_before': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Stock']"}),
            'stock_exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.StockExchange']"})
        }
    }

    complete_apps = ['app']