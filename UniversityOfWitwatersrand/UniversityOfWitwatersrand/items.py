# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def clean_string(var):
    var = str(var)
    var = var.lstrip() #removes initial space
    var = var.lstrip() #removes initial space
    var = var.rstrip()
    var = var.replace('\"', '').rstrip()
    var = var.replace('\n', '').rstrip()
    var = var.replace('\\n', '').rstrip()
    var = var.replace('\xa0','').rstrip()
    var = var.replace('\\xa0','').rstrip()
    var = var.replace('\n\t\xa0', '').rstrip()
    var = var.replace('\t', '').rstrip()
    var = var.replace('\\t', '').rstrip()
    var = var.replace('\u2010','').rstrip()
    var = var.replace('\u2011','').rstrip()
    var = var.replace('\u2012','').rstrip()
    var = var.replace('\u2013','').rstrip()
    var = var.replace('\u2014','').rstrip()
    var = var.replace('\u2015','').rstrip()
    var = var.replace('\u2016','').rstrip()
    var = var.replace('\u2017', '').rstrip()
    var = var.replace('\u2018', '').rstrip()
    var = var.replace('\u2019', '').rstrip()
    var = var.replace('\u2020', '').rstrip()
    var = var.replace('\u2021', '').rstrip()
    var = var.replace('\u2022','').rstrip()
    var = var.replace('\r\n\r\n\u2022\t', '').rstrip()
    var = var.replace('\r\n\r\n', '').rstrip()
    var = var.replace('\r\n', '').rstrip()
    var = var.replace('\r\n\u2022', '').rstrip()
    var = var.replace('\\r', '').rstrip()
    var = var.replace('\r', '').rstrip()
    var = var.replace('\r\t', '').rstrip()
    var = var.replace('\r\r', '').rstrip()
    var = var.replace('\r\r\t', '').rstrip()
    var = var.replace('\u00ae', '').rstrip()
    var = var.replace('\u00ac', '').rstrip()
    var = var.replace('\u00a0\u00a0', '').rstrip()
    var = var.replace('\u201c', '').rstrip()
    var = var.replace('\u201d', '').rstrip()
    var = var.replace('\u201f', '').rstrip()
    var = var.replace('\u00b4', '').rstrip()
    return var 


class UniversityItem(scrapy.Item):
    university = scrapy.Field() 
    logo = scrapy.Field()
    location = scrapy.Field()
    language = scrapy.Field()
    phone = scrapy.Field()
    mail = scrapy.Field()
    website = scrapy.Field()

class DetailsItem(scrapy.Item):  
    varsity = scrapy.Field()
    school = scrapy.Field()
    level = scrapy.Field()
    programme = scrapy.Field()
    study_mode = scrapy.Field()
    eligibility_criteria = scrapy.Field()
    intake = scrapy.Field()
    duration = scrapy.Field()
    img = scrapy.Field()
    programme_description = scrapy.Field()
    
class FeesItem(scrapy.Item):
    university = scrapy.Field() 
    