"""Scrape metadata attributes from a requested URL."""
from typing import Optional
import requests
from bs4 import BeautifulSoup
from requests import Response
import ua_generator
from rich import inspect, print as rprint

# ua = ua_generator.generate()

class GetMeta:
    def __init__(self, url):
        self.url = url
        self.ua = ua_generator.generate()
        self.headers = self.ua.headers.get()
        self.html = self.url_response()
        self.soup = self.get_soup()
        # self.response = self.make_request()
    
    def url_response(self):
        ua = ua_generator.generate()
        try:     
            response = requests.get(self.url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        # inspect(response)   
        return response.text
    
    def get_soup(self):
        response = self.url_response()
        soup = BeautifulSoup(response, 'html.parser')    
        # head = soup.head
        # body = soup.body
        # foot = soup.footer
        return soup    

    def get_head(self):    
        soup = self.get_soup()
        head = soup.head
        return head
    
    def get_body(self):    
        soup = self.get_soup()
        body = soup.body
        return body    
    
    def get_footer(self):    
        soup = self.get_soup()
        footer = soup.footer
        return footer
    
    def get_meta(self):    
        soup = self.get_soup()
        meta = soup.find_all('meta')
        return meta   
    
    def select_body_links(self):
        body = self.get_body()
        a = body.find_all('a')
        return a
    
    def select_main(self):
        soup = self.get_soup()
        main = soup.select("#main")
        # print(main)
        return main
        
    def select_paragraphs(self):
        soup = self.get_soup()
        pg = soup.select("div p")
        # print(pg)
        return pg
        # print(main)        
    
    
    
    
    # def print_soup(self):
    #     soup = self.get_soup()
    #     print(soup.name)
    #     print(soup.head)
        
    
    
if __name__ == "__main__":
    url = 'https://electronicintifada.net/blogs/maureen-clare-murphy/uneasy-equilibrium-after-israel-strikes-iran'
    x = GetMeta(url=url)
    inspect(x.select_paragraphs())
    
    
    
    
    # inspect(y, all=True)
    # meta = x.scrape_page_metadata()
    # inspect(meta)          