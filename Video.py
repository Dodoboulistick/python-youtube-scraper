from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
import os

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
        self.title, self.author, self.description, self.likes, self.exists = self.get_video_info(self.soup)
        self.links = self.get_links(self.description, self.exists)

    def get_page(self, url: str) -> BeautifulSoup:
        session = HTMLSession()
        response = session.get(url)
        response.html.render(sleep=4)
        soup = BeautifulSoup(response.html.html, 'lxml')
        
        return soup

    def get_video_info(self, soup: BeautifulSoup) -> tuple:
        try:
            title = soup.findAll('div')[0].find("meta", {"itemprop": "name"}).get("content")
            print(title)
            author = soup.findAll('div')[0].find("link", {"itemprop": "name"}).get("content")
            print(author)
            description_raw = soup.find(id="description-inline-expander").find("yt-formatted-string").contents
            description = os.linesep.join([s for s in description_raw.splitlines() if s])
            print(description)
            likes_raw = str(soup.select_one('button.yt-spec-button-shape-next--icon-leading > '
            '.yt-spec-button-shape-next--button-text-content > span.yt-core-attributed-string').contents[0])
            likes = re.sub(r'\xa0',"", likes_raw)
            print(likes)
            exists = True
        except:
            title = ""
            author = ""
            description = ""
            likes = 0
            exists = False
        return title, author, description, likes, exists

    def get_links(self, description: str, exists: bool) -> list:
        if(exists):
            links = re.findall(r'(https?://\S+)', description)
        else:
            links = []
        return links
    
    def __str__(self) -> str:
        return f"Title: {self.title}\nAuthor: {self.author}\nDescription: {self.description}\nLinks: {self.links}\nLikes: {self.likes}\nExists: {self.exists}"