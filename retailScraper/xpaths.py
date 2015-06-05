class PathsHolder():
	xPaths = {
		'macys': {
			'title': '//*[@id="productTitle"]/text()',
			'price': '//div[@class="standardProdPricingGroup"]//span[@class="priceSale"]/text()'
		},
		'zales': {
			'title': '//div[@id="productTitle"]/text()',
			'price': '//td[@id="productPriceCell"]/div[2]/text()'
		},
		'kay': {
			'title': '//h1[@class="product-name"]/text()',
			'price': '//div[@class="prices-and-info clearfix"]//p[@class="price"]/text()'
		},
		'helzberg': {
			'title': '//div[@class="product-detail"]/h2/text()',
			'price': '//span[@class="current"]/text()'
		},
		'bluenile': {
			'title': '//h1[@class="offer-name page-title"]/text()',
			'price': '//span[@class="price"]/text()'
		}
	}