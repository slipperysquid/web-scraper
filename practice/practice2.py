import sys
sys.path.append('../web-scraper')
from scraper import scraper


scrape = scraper("http://olympus.realpython.org/login")

form = scrape.getTag("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
scrape.submitForm(form)

print(scrape.page.url)

