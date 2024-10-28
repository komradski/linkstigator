# import sqlite3
# from modeltest import views as v
# from bs4 import BeautifulSoup
import bs4
# import requests
from urllib.request import urlopen as request
import re
from rich import inspect, print as rprint

from bs4 import BeautifulSoup as soup
from bs4 import SoupStrainer as strainer

url = 'https://electronicintifada.net/blogs/maureen-clare-murphy/uneasy-equilibrium-after-israel-strikes-iran'

link = 'https://apnews.com/article/florida-orlando-suitcase-death-guilty-verdict-trial-33728cc7788c0f4e28aae0b0c85df346'

thing = '<div class="RichTextStoryBody RichTextBody">'


client = request(url)
page_html = client.read()
client.close()

only_item_cells = strainer("div", attrs={"class": "item-cell"})
page_soup = soup(page_html, 'html.parser', parse_only=only_item_cells)
page_soup_list = list(page_soup)


for poo in page_soup_list:
    print(poo)


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
    