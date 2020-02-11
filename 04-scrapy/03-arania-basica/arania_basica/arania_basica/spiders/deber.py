import scrapy
import numpy
import pandas as pd
import pickle
from re import sub

class IntroSpider(scrapy.Spider):
    name = 'homework_spider'
    urls = ['http://books.toscrape.com/catalogue/category/books_1/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url)
            

    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        # Ejercicio 0 títulos
        titulos = etiqueta_contenedora.css('h3 > a::attr(title)').extract()
        # Ejercicio 1 links de imágenes
        links_to_images = etiqueta_contenedora.css('div > a::attr(href)').extract()
        links = []
        for link in links_to_images:
            links.append(response.urljoin(link))
        # Ejercicio 2
        prices = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        prices_float = map(lambda money: float(sub(r'[^\d.]', '', money)), prices)
        
        #Convert to dataset        
        serie_titulos = pd.Series(titulos)
        serie_links = pd.Series(links)
        serie_prices = pd.Series(list(prices_float))
        
        df = serie_titulos.to_frame(name='Titulo')
        df['Links'] = serie_links
        df['Prices'] = serie_prices
        df.to_csv('./results.csv',mode='a', header=False)

        # Ejercicio 3
        etiqueta_contenedora = response.css('div.side_categories')
        side_categories_links = etiqueta_contenedora.css('li > ul > li > a::attr(href)').extract()
        links = []
        for link in side_categories_links:
           links.append(response.urljoin(link))
        for link in links:
            yield scrapy.Request(link)