from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup
import re



class scraper():

    def __init__(self):
        pass

    def __init__(self, url):#if specific website is provided
        self.url = url
        self.browser = mechanicalsoup.Browser()
        self.page = self.browser.get(url)
        self.soup = self.page.soup


    def setSite(self, url):#sets current website to the url provided
        self.url = url
        self.browser = mechanicalsoup.Browser()
        self.page = self.browser.get(url)
        self.soup = self.page.soup


    def getHtml(self):#retuns the html of the current website
        return self.soup

    def getImages(self):#returns a list of image tag objects that are on the webpage
        return self.soup.find_all("img")

    def getTag(self, tag):#returns all instances of a certain html tag
        return self.soup.find_all(tag)


    def getTitle(self):#returns the title of the current website
        return self.soup.title.string
    
    def submitForm(self, form):#submits a form to the opened page
        self.page = self.browser.submit(form, self.page.url)
        self.soup = self.page.soup

