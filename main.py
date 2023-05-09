import requests
import selectorlib
from email_module import send_email

URL = "http://programmer100.pythonanywhere.com/tours/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape page source from url"""
    response = requests.request('GET',url,headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value

if __name__ == "__main__":
    
    Event = extract(scrape(URL))
    
    if Event != 'No upcoming tours':
        send_email()

    print(extract(scrape(URL)))