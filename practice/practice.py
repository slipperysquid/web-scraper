import sys
sys.path.append('../web-scraper')
from scraper import scraper

base_link = "http://olympus.realpython.org"
scrape = scraper("http://olympus.realpython.org/profiles")
tag_list = scrape.getTag("a")
for tag in tag_list:
    print(base_link+tag["href"])
