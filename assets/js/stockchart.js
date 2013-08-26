$(function() {
    var dataUrl = $('#stockchart').attr('data-url')

    if (dataUrl) {
        $.getJSON(dataUrl, function(response) {

		// split the data set into ohlc and volume
		var ohlc = [],
			volume = [],
            data = response.data,
			dataLength = data.length;

		for (var i = 0; i < dataLength; i++) {
			ohlc.push([
				data[i]['date'], // the date
				data[i]['open'], // open
				data[i]['high'], // high
				data[i]['low'], // low
				data[i]['close'] // close
			]);

			volume.push([
				data[i]['date'], // the date
				data[i]['volume'] // the volume
			])
		}

		// set the allowed units for data grouping
		var groupingUnits = [[
			'week',                         // unit name
			[1]                             // allowed multiples
		], [
			'month',
			[1, 2, 3, 4, 6]
		]];

		// create the chart
		$('#stockchart').highcharts('StockChart', {

		    rangeSelector: {
		        selected: 1
		    },

		    title: {
		        text: response.name
		    },

		    yAxis: [{
		        title: {
		            text: 'OHLC'
		        },
		        height: 200,
		        lineWidth: 2
		    }, {
		        title: {
		            text: 'Volume'
		        },
		        top: 300,
		        height: 100,
		        offset: 0,
		        lineWidth: 2
		    }],

		    series: [{
		        type: 'candlestick',
		        name: response.name,
		        data: ohlc,
		        dataGrouping: {
					units: groupingUnits
		        }
		    }, {
		        type: 'column',
		        name: 'Volume',
		        data: volume,
		        yAxis: 1,
		        dataGrouping: {
					units: groupingUnits
		        }
		    }]
		});
	});
    }


});