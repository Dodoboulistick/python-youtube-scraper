import requests
import json
from bs4 import BeautifulSoup
import re

class Video:
    url: str
    soup: BeautifulSoup
    title: str
    author: str
    description: str
    links: list
    likes: int
    exists: bool

    def __init__(self, url: str) -> None:
        self.url = url
        self.soup = self.get_page(url)
        self.title, self.author, self.description, self.exists = self.get_video_info(self.soup)
        self.links = self.get_links(self.description, self.exists)

    def get_page(self, url: str) -> str:
        query = requests.get(url).content
        soup = BeautifulSoup(query, 'html.parser')
        return soup

    def get_video_info(self, soup: BeautifulSoup) -> tuple:
        try:
            firstscript = soup.find('body').find('script').text[:-1].split("var ytInitialPlayerResponse = ")[1]
            firstscriptJSON = json.loads(firstscript)
            title = firstscriptJSON['videoDetails']['title']
            author = firstscriptJSON['videoDetails']['author']
            description = firstscriptJSON['videoDetails']['shortDescription']
            exists = True
        except:
            title = ""
            author = ""
            description = ""
            exists = False
        return title, author, description, exists

    def get_links(self, description: str, exists: bool) -> list:
        if(exists):
            links = re.findall(r'(https?://\S+)', description)
        else:
            links = []
        return links
    
    def __str__(self) -> str:
        return f"Title: {self.title}\nAuthor: {self.author}\nDescription: {self.description}"