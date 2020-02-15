# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def transformar_url_imagen(texto):
    url_fybeca = 'https://fybeca.com'
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar, url_fybeca)

def extraer_precio(texto):
    price = re.findall(r"(?<=\()[^\d]*\d+\.\d{2}[^\d]*(?=\))", texto)
    return float(price[0])


class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
        ),
        output_processor = TakeFirst()
    )
    precio_VC = scrapy.Field(
        input_processor = MapCompose(
            extraer_precio
        ),
        output_processor = TakeFirst()
    ) 
    precio_normal = scrapy.Field(
        input_processor = MapCompose(
            extraer_precio
        ),
        output_processor = TakeFirst()
    ) 
    ahorro = scrapy.Field()


class AraniaFibecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
