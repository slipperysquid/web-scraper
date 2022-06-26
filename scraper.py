from urllib.request import urlopen
import re



class scraper():

    def __init__(self):
        pass

    def __init__(self, url):#if specific website is provided
        self.url = url
        self.page = urlopen(url)
        self.html_bytes = self.page.read()
        self.html = self.html_bytes.decode("utf-8")
        
    def setSite(self, url):#sets current website to the url provided
        self.url = url
        self.page = urlopen(url)
        self.html_bytes = self.page.read()
        self.html = self.html_bytes.decode("utf-8")

    def getHtml(self):#retuns the html of the current website
        return self.html

    def getTitle(self):#returns the title of the current website
        match_results = re.search("<title.*?>.*?<title.*? n>", self.html, re.IGNORECASE)
        title = match_results.group()
        title = re.sub("<.*?>", "", title)#remove html tags
        return title


