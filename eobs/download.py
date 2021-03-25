import os
import requests
from bs4 import BeautifulSoup

ACCESS = 'https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php'
ACCESS_MONTHS = 'https://surfobs.climate.copernicus.eu/dataaccess/access_eobs_months.php'

def get_urls(url):
    soup = BeautifulSoup(requests.get(url).text)
    filt = filter(lambda a: ('href' in a.attrs) and (a['href'].endswith('.nc')), soup.find_all('a'))
    return [a['href'] for a in filt]

all_urls = get_urls(ACCESS) + get_urls(ACCESS_MONTHS)
fh = open('download.aria', 'w')
for url in all_urls:
    print(url, file=fh)
    name=os.path.basename(url)
    print('  out=data/{}\n'.format(name), file=fh)
fh.close()
