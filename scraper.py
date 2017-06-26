import scrapy
from bs4 import BeautifulSoup as bSoup
from pymongo import MongoClient


class ScrapNykaa(scrapy.Spider):

    name = "scrapper"

    def start_requests(self):
        for i in range(1, 25):
            yield scrapy.Request('http://www.nykaa.com/personal-care-appliances.html?p=%s&isAjax=1' % str(i))

    def parse(self, response):
        self.parsers(response.text)

    def parsers(self, text_response):
        soup = bSoup(text_response, 'html.parser')
        p = soup.find_all('li', attrs={'class': 'n_prod_block'})
        self.scrape_ids(p)

    def scrape_ids(self, p):
        for i in range(len(p)):
            px = p[i]
            product_name = px.get('id').split('-')[len(px.get('id').split('-')) - 1]
            img_attr = px.find('div', class_='product-image')
            img_attr_a = img_attr.find('a', class_='product-image')
            product_title = img_attr_a.get('title')
            img_link = img_attr_a.find('img', class_='lazy').get('data-original')
            post_info = {"product_id": "product_id_" + str(product_name) + "", "img_link":"" + img_link + "", "product_title":"" + product_title + "" }
            self.mongo_db_credentials(post_info)

    def mongo_db_credentials(self, post_data):
        post_ids=[]
        url = 'mongodb://localhost:27017/'
        client = MongoClient(url)
        db = client['nykaa_db']
        posts = db.posts
        post_id = posts.insert_one(post_data).inserted_id
        post_ids.append(post_id)
        print('Store updated')
        client.close()
