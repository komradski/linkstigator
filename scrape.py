# import sqlite3
# from modeltest import views as v
# from bs4 import BeautifulSoup
import bs4
import requests
# from urllib.request import urlopen as request
import re
from rich import inspect, print as rprint

from bs4 import BeautifulSoup
from bs4 import SoupStrainer as strainer
import ua_generator

ua = ua_generator.generate()



url = 'https://electronicintifada.net/blogs/maureen-clare-murphy/uneasy-equilibrium-after-israel-strikes-iran'

link = 'https://apnews.com/article/florida-orlando-suitcase-death-guilty-verdict-trial-33728cc7788c0f4e28aae0b0c85df346'

thing = '<div class="RichTextStoryBody RichTextBody">'

# client = request(url)
# page_html = client.read()
# client.close()

only_item_cells = strainer("div", attrs={"class": "item-cell"})

class GetSoup:
    def __init__(self, url):
        self.url = url
        # self.response = self.make_request()
    
    def make_request(self):
        ua = ua_generator.generate()
        try:     
            response = requests.get(self.url, headers=ua.headers.get())
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        # inspect(response)   
        return response.text
    
    def get_soup(self):
        response = self.make_request()
        soup = BeautifulSoup(response, 'html.parser')            
        return soup
    
    # def get_meta(self):
    #     html = self.get_soup()
    #     metadata = {
    #     "title": get_title(html),
    #     "description": get_description(html),
    #     "image": get_image(html),
    #     "favicon": get_favicon(html, url),
    #     "theme_color": get_theme_color(html),
    # }
    # return metadata
        
    
    def get_og_meta(self):
        # works with ei url
        soup = self.get_soup()
      
        site_name = soup.find("meta", property="og:site_name").get('content')
        type = soup.find("meta", property="og:type").get('content')
        title = soup.find("meta", property="og:title").get('content')
        url = soup.find("meta", property="og:url").get('content')
        description = soup.find("meta", property="og:description").get('content')
        updated_type = soup.find("meta", property="og:updated_time").get('content')
        image = soup.find("meta", property="og:image").get('content')
        print(site_name)
        print(type)
        print(title)
        print(url)
        print(description)
        print(updated_type)
        print(image)
        
        # return meta
    
    def print_pretty_soup(self):
        soup = self.get_soup()
        rprint(soup)
        # rprint(soup.prettify)
    
if __name__ == "__main__":
    x = GetSoup(url=link)
    meta = x.get_og_meta()
    # for z in meta:
    #     rprint(z.get('content'))
    # inspect(meta)



# <meta property="og:image" content="https://electronicintifada.net/sites/default/files/styles/medium/public/pictures/picture-15-1457643566.jpg?itok=2gPGktTn" />


# <meta name="description" content="Tehran and Tel Aviv both claim tactical success over limited attack." />
# <meta name="generator" content="bangpound" />
# <link rel="canonical" href="https://electronicintifada.net/blogs/maureen-clare-murphy/uneasy-equilibrium-after-israel-strikes-iran" />
# <link rel="shortlink" href="https://electronicintifada.net/node/49671" />



# x.make_request()
# soup = x.get_soup()
# title = soup.find("meta", property="og:title")
# url = soup.find("meta", property="og:url")

# print(title)
# print(url)

# soup = x.get_soup()  
# inspect(soup)



# for poo in page_soup_list:
#     print(poo)


# def strain():
#     client = requests.get(link)        
#     only_item_cells = strainer("meta")
#     page_soup = soup(client, 'html.parser', parse_only=only_item_cells)
#     page_soup_list = list(page_soup)
#     print(page_soup_list)

# strain()

# def get_meta():
#     response = requests.get(link)
#     html_data = response.text
#     soup = BeautifulSoup(html_data, "html.parser")
    
#     for x in soup:
#         z = x.find("meta")
#         print(z)
    
    # metas = soup.find("meta")
    # print(metas)
    # for meta in metas:
    #     print(meta)
    # title = soup.find("meta", property="og:title")
    # url = soup.find("meta", property="og:url")

    # print(title["content"] if title else "No meta title given")
    # print(url["content"] if url else "No meta url given")






# get_meta()

















# import get_link_object
# , Organization 

# database = 'db.sqlite3'

# conn = sqlite3.connect(database)

# import sqlite3

# def organization_all():
#     try:
#         with sqlite3.connect(database) as conn:
#             cur = conn.cursor()
#             cur.execute('SELECT * FROM modeltest_organization')
#             rows = cur.fetchall()
#             # for row in rows:
#             #     print(row)
#     except sqlite3.Error as e:
#         print(e)
#     return rows

# def link_all():
#     try:
#         with sqlite3.connect(database) as conn:
#             cur = conn.cursor()
#             cur.execute('SELECT * FROM modeltest_link')
#             rows = cur.fetchall()
#             # for row in rows:
#             #     print(row)
#     except sqlite3.Error as e:
#         print(e)
#     return rows

# for x in link_all():
#     print(x)

# links = v.get_link_object()

# for link in links():
#     print(link.url)
    