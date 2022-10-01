from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib.request
import re
import time
import locale

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

initial_time = time.time()
rounds = 0

while True:
    try:
        if rounds < 5:
            data = urllib.request.urlopen('https://www.bing.com/search?q=usd+to+ugx')
            only_p_tags = SoupStrainer('p')
            soup = BeautifulSoup(data, 'lxml', parse_only=only_p_tags)
            output = round(locale.atof(soup.find(string=re.compile("1.00 US Dollar")).split("= ")[1].split()[0].replace(",", "")))
            if output:
                break
            else:
                rounds += 1
                time.sleep(1)
        else:
            break
    except Exception as e:
        rounds += 1
        print(e)
        time.sleep(1)

if output:
    print(output)
print(round(time.time() - initial_time))