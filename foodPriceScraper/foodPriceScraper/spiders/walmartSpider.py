import scrapy

class walmartSpider(scrapy.Spider):
    name = "walmart"
    start_urls = ["https://www.walmart.com/search?q=tofu"]
    
    def parse(self, response):
        
        item_div = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div'
        name = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/span/span'
        img = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[1]/div[1]'
        price = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[1]/div[1]'
        price_per_unit = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[1]/div[2]'
        rating = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[2]/span[3]'
        rating_count = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[2]/span[2]'
        ebt = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[3]/span'
        pickup = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[6]/span[2]'
        delivery = '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div[1]/section/div/div[1]/div/div/div/div[2]/div[6]/span[3]'
        
        for item in response.xpath(item_div).getAll():
            try:
                yield{
                    "name" : item.xpath(name.replace(item_div,"")).get(),
                    "img" : item.xpath(img.replace(item_div, "")).get(),
                    "price" : item.xpath(price.replace(item_div, "")).get(),
                    "price_per_unit" : item.xpath(price_per_unit.replace(item_div, "")).get(),
                    "rating" : item.xpath(rating.replace(item_div, "")).get(),
                    "rating_count" : item.xpath(rating_count.replace(item_div, "")).get(),
                    "ebt" : item.xpath(ebt.replace(item_div, "")).get(),
                    "pickup" : item.xpath(pickup.replace(item_div, "")).get(),
                    "delivery" : item.xpath(delivery.replace(item_div, "")).get(),
                }
            except:
                pass