# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

"""
id为slider_ct_name的h4元素获取
日期可以通过获取id为blk_fc_c0_scroll下的class为wt_fc_c0_i_date的p元素获取
天气描述可以通过获取id为blk_fc_c0_scroll下的class为icons0_wt的img元素获取
温度可以通过获取id为blk_fc_c0_scroll下的class为wt_fc_c0_i_temp的p元素获取
"""
class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    date = scrapy.Field()
    dayDesc = scrapy.Field()
    dayTemp = scrapy.Field()
    pass
