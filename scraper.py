from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



class scraper():

    def __init__(self):
        pass

    def __init__(self, url):#if specific website is provided
        self.url = url
        self.page = urlopen(url)
        self.html_bytes = self.page.read()
        self.html = self.html_bytes.decode("utf-8")
        self.soup = BeautifulSoup(self.html, "html.parser")

    def setSite(self, url):#sets current website to the url provided
        self.url = url
        self.page = urlopen(url)
        self.html_bytes = self.page.read()
        self.html = self.html_bytes.decode("utf-8")
        self.soup = BeautifulSoup(self.html, "html.parser")

    def getHtml(self):#retuns the html of the current website
        return self.html

    def getImages(self):#returns a list of image tag objects that are on the webpage
        return self.soup.find_all("img")

    def getTag(self, tag):#returns all instances of a certain html tag
        return self.soup.find_all(tag)


    def getTitle(self):#returns the title of the current website
        return self.soup.title.string


