import scrapy 
from zhilian.items import ZhilianItem



class zhilianspiderSpider(scrapy.Spider):
    name='zhilianSpider'
    allowed_domains=['www.zhipin.com']

    start_urls=['https://www.zhipin.com/c101010100/?query=web%E5%89%8D%E7%AB%AF&industry=&position=&ka=hot-position-4']

    front='https://www.zhipin.com'
    def parse(self,response):
        jobTitle=response.xpath("//div[@class='info-primary']//div[@class='job-title']/text()").extract()
        print('======================================')
        print(jobTitle)
        

        company=response.xpath("//div[@class='info-company']/div/h3/a/text()").extract()

        print('======================================')
        print(company)

        links=response.xpath("//div[@class='info-primary']/h3[@class='name']/a/@href").extract()

        print('======================================')

        print(links)

        # print(jobTitle,company,links)
        
        for jobTitle1,company1,links1 in zip(jobTitle,company,links):
            data={'jobTitle1':jobTitle1,'company1':company1,'links1':self.front+links1}
            print('=======================')
            print(data)

            
            yield   scrapy.Request(links1,meta={'data':data},callback=self.getinformation)
            # links1 = self.front + links1
            # print(jobTitle1,company1,links1)


    def getinformation(self,response):
    #     data=response.meta['data']
    #     jobTitle1=data['jobTitle1']
    #     links1=data['links1']
    #     print('====================')
    #     print(links1)
    #     xinxi=[]

    #     if True:
    #         xinxi+=response.xpath("//div[@class='detail-content']/div[@class='job-sec']/div[@class='text']")
    #         print("==================")

    #         print(xinxi)





           

