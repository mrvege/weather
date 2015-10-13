# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
每个item pipeline组件(有时称之为“Item Pipeline”)是实现了简单方法的Python类。他们接收到Item并通过它执行一些行为，同时也决定此Item是否继续通过pipeline，或是被丢弃而不再进行处理。
item pipeline的典型应用有：
清理HTML数据
验证爬取的数据(检查item包含某些字段)
查重(并丢弃)
将爬取结果保存到文件或数据库中
"""
class WeatherPipeline(object):
    def __init__(self):
        self.file = open('wea.txt', 'w+')
    def process_item(self, item, spider):
        city = item['city'][0].encode('utf-8')
        self.file.write('city:' + str(city) +'\n\n')
        date = item['date']
        desc = item['dayDesc']
        dayDesc = desc[1::2]
        nightDesc = desc[0::2]
        dayTemp = item['dayTemp']
        weaitem = zip(date, dayDesc, nightDesc, dayTemp)
        for i in range(len(weaitem)):
            item = weaitem[i]
            d = item[0]
            dd = item[1]
            nd = item[2]
            ta = item[3].split('/')
            dt = ta[0]
            nt = ta[1]
            txt = 'data:{0}\t\tday:{1}({2})\t\tnight:{3}({4})\n\n'.format(
            d,
            dd.encode('utf-8'),
            dt.encode('utf-8'),
            nd.encode('utf-8'),
            nt.encode('utf-8')
            )
            self.file.write(txt)
        return item
