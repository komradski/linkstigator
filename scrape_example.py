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
        self.html = self.get_content()
        # self.response = self.make_request()
    
    def get_content(self):
        ua = ua_generator.generate()
        try:     
            response = requests.get(self.url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        # inspect(response)   
        return response.text



    def scrape_page_metadata(self):
        """
        Parse page & return metadata.

        :param Response resp: Raw HTTP response.
        :param str url: URL of targeted page.

        :return: dict
        """
        # html = BeautifulSoup(resp.content, "html.parser")
        metadata = {
            "title": self.get_title(self.html),
            # "description": self.get_description(self.html),
            # "image": self.get_image(self.html),
            # "favicon": self.get_favicon(self.html),
            # "theme_color": self.get_theme_color(self.html),
        }
        return metadata


    def get_title(self):
        """
        Scrape page title with multiple fallbacks.

        :param BeautifulSoup html: Parsed HTML object.
        :param str url: URL of targeted page.

        :returns: Optional[str]
        """
        title = self.html.title
        if title:
            return title
        elif self.html.find("meta", property="og:title"):
            return self.html.find("meta", property="og:title").get("content")
        return self.html.find("h1")


    def get_description(self) -> Optional[str]:
        """
        Scrape page description.

        :param BeautifulSoup html: Parsed HTML object.
        :param str url: URL of targeted page.

        :returns: Optional[str]
        """
        description = self.html.find("meta", property="description")
        if description:
            return description.get("content")
        elif self.html.find("meta", property="og:description"):
            return self.html.find("meta", property="og:description").get("content")
        return self.html.p.string


    def get_image(self) -> Optional[str]:
        """
        Scrape preview image.

        :param BeautifulSoup html: Parsed HTML object.

        :returns: Optional[str]
        """
        image = self.html.find("meta", property="image")
        if image:
            return image.get("content")
        elif self.html.find("meta", {"property": "og:image"}):
            return self.html.find("meta", {"property": "og:image"}).get("content")
        return self.html.img.src


    def get_favicon(self) -> Optional[str]:
        """
        Scrape favicon from `icon`, or fallback to conventional favicon.

        :param Response resp: Raw HTTP response.
        :param str url: URL of targeted page.

        :returns: Optional[str]
        """
        if self.html.find("link", attrs={"rel": "icon"}):
            return html.find("link", attrs={"rel": "icon"}).get("href")
        elif self.html.find("link", attrs={"rel": "shortcut icon"}):
            return self.html.find("link", attrs={"rel": "shortcut icon"}).get("href")
        return f"{self.url.rstrip('/')}/favicon.ico"


    def get_theme_color(self) -> Optional[str]:
        """
        Scrape brand color.

        :param BeautifulSoup html: Parsed HTML object.

        :returns: Optional[str]
        """
        if self.html.find("meta", {"name": "theme-color"}):
            return self.html.find("meta", {"name": "theme-color"}).get("content")
        
        
if __name__ == "__main__":
    url = 'https://electronicintifada.net/blogs/maureen-clare-murphy/uneasy-equilibrium-after-israel-strikes-iran'
    x = GetMeta(url=url)
    y = x.get_title()
    inspect(y, all=True)
    # meta = x.scrape_page_metadata()
    # inspect(meta)      