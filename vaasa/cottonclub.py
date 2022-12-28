import re
import urllib.request
from bs4 import BeautifulSoup as soup
from datetime import datetime, date
from restaurants import restaurants


class Cotton:
    name = "Cotton Club"
    icon = ":cloud:"
    url = "https://www.cotton-club.fi/ruokalista"

    def getList(self) -> list[str]:
        menu = []

        index_url = 'https://www.cotton-club.fi/ruokalista'
        response = urllib.request.urlopen(index_url)
        content = response.read()

        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(content)
            f = gzip.GzipFile(fileobj=buf)
            content = f.read()

        parser = soup(content, 'html.parser')

        todays_date = '{dt.day}.{dt.month}'.format(dt=datetime.today())

        for pricelist in parser.select('.pricelist'):
            is_today = False
            is_salad = False
            headline = pricelist.select_one('.headline').get_text()

            match = re.search(r'viikon.*salaatti',
                              headline, flags=re.IGNORECASE)

            if match:
                is_salad = True

            match = re.search(r'(\d+\.\d+)\.?', headline)

            if match:
                is_today = match.group(1) == todays_date

            if is_today or is_salad:
                for item in pricelist.select('.item .itemname'):
                    text = item.get_text().strip()
                    text = re.sub(r'\([VLG,]+\)|S$', '', text).strip()

                    if is_salad:
                        text = 'Viikon salaatti: ' + text

                    if text:
                        menu.append(text)

        return menu


def initialize() -> None:
    restaurants.register("cottonclub", Cotton)
