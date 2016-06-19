from time import sleep
from urllib import request
from bs4 import BeautifulSoup


class SurugayaParser():
    BASE_URL = 'http://www.suruga-ya.jp/search'

    def __init__(self):
        self.is_firstrequest = True

    def request_items(self, pages=1, sleepsec=1):
        return list(self._item_generator(pages, sleepsec))

    def set_target_url(self, params):
        url = self.BASE_URL + '?' + params
        self.target_url = url

    def _item_generator(self, pages, sleepsec):
        for p in range(1, pages+1):
            self._sleep_if_not_firsttime(sleepsec)
            for item in self._parse_from_url(page=p):
                yield item

    def _sleep_if_not_firsttime(self, sleepsec):
        if self.is_firstrequest:
            self.is_firstrequest = False
        else:
            sleep(sleepsec)

    def _parse_from_url(self, page=1):
        url = self.target_url + '&page=' + str(page)
        html = request.urlopen(url)
        return self._parse_html(html)

    def _parse_html(self, html):
        soup = BeautifulSoup(html, 'lxml')
        items = self._find_items(soup)
        return (self._parse_item(i) for i in items)

    def _find_items(self, soup):
        return soup.find('body').findAll(class_='item')

    def _parse_item(self, item):
        return {
            'title': self._find_class(item, 'title'),
            'maker': self._find_class(item, 'maker'),
            'price': self._find_class(item, 'price'),
            'price_teika': self._find_class(item, 'price_teika'),
            'link': self._find_link(item),
            'picture': self._find_picture(item)
            }

    def _find_class(self, item, class_):
        raw = item.find(class_=class_)
        if raw is None:
            return None
        else:
            return raw.text.replace('\xa0', '')  # priceから'\xa0'を削除

    def _find_link(self, item):
        raw = item.find(class_='photo_box')
        return raw.find('a').get('href')

    def _find_picture(self, item):
        img = item.find(class_='photo_box').find('img')
        img_url = img.get('src')
        return img_url.replace('&size=m', '&size=l')  # 大きいサイズ
