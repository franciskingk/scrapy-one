from flask import request
import scrapy
from scrapy import Spider 
from scrapy.http import Request
from UniversityOfWitwatersrand.items import UniversityItem,DetailsItem,clean_string



class WitsSpider(Spider):
    name = 'WITS'
    allowed_domains = ['wits.ac.za']
    start_urls =('http://wits.ac.za/','https://www.wits.ac.za/clm/')


    def start_requests(self):
        for url in self.start_urls:
            if url == 'https://www.wits.ac.za/clm/':
                yield Request(url,callback=self.parse_clm)
            else:
                yield Request(url,callback=self.parse_home)    

# faculty of commerce law and management
    def parse_clm(self,response):
        url = response.urljoin(response.xpath('/html/body/div[2]/main/header[3]/section[1]/nav[2]/div/ul/li[2]/a/@href').extract_first())
        yield Request(url,callback = self.parse_clm_under) #clm undergraduate

    def parse_clm_under(self,response):
        url = response.urljoin(response.xpath('//*[@class="side-nav"]/li/a/@href').extract_first())
        yield Request(url,callback=self.parse_clm_list)    #program list
    
    def parse_clm_list(self,response):
        Level= 'Undergraduate'
        School= response.xpath('/html/body/div[2]/main/header[3]/h2/text()').extract_first()
        items = response.xpath('//*[@class="card-style-result"]/a')
        for item in items:
            Programme= item.xpath('./h3/text()').extract_first()
            Duration= item.xpath('./div[2]/ul/li[2]/text()').extract_first()
            Study_mode= item.xpath('./div[2]/ul/li[3]/text()').extract_first()
            img = response.urljoin(item.xpath('./div[1]/img/@src').extract_first())
            url=response.urljoin(item.xpath('./@href').extract_first())
            #yield{'Programme':Programme,'Duration':Duration,'Study_mode':Study_mode,'Level':Level,'School':School,'img':img}
            yield Request(url,callback=self.parse_clm_list_detail,meta={'Programme':Programme,'Duration':Duration,'Study_mode':Study_mode,'Level':Level,'School':School,'img':img})

        next_page = response.urljoin(response.xpath('//ul[@class="pagination"]/li[3]/a[2]/@href').extract_first())
        yield Request(next_page,callback=self.parse_clm_list) 
       
    def parse_clm_list_detail(self,response):
        item=DetailsItem()
        Programme=response.meta.get('Programme')
        Duration=response.meta.get('Duration')
        Study_mode=response.meta.get('Study_mode')
        Level=response.meta.get('Level')
        School=response.meta.get('School')
        img=response.meta.get('img')

        Programme_description = response.xpath('//*[@id="panel1"]//text()').extract()
        Eligibility_criteria = response.xpath('//*[@id="panel3"]//text()').extract()
        #yield{'Programme_description':Programme_description,'Eligibility_criteria':Eligibility_criteria,'Programme':Programme,'Duration':Duration,'Study_mode':Study_mode,'Level':Level,'School':School,'img':img}
        item['school']=clean_string(School)
        item['level']=clean_string(Level)
        item['programme']=clean_string(Programme)
        item['study_mode']=clean_string(Study_mode)
        item['eligibility_criteria']=clean_string(Eligibility_criteria)
        #item['intake']=clean_string(Intake)
        item['duration']=clean_string(Duration)
        item['img']=clean_string(img)
        item['programme_description']=clean_string(Programme_description)
        #yield item 


        

    def parse_home(self,response):

        pass

