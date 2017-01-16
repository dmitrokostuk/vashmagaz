
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from lxml.html import fromstring


def get_text(node, class_name):
    el = node.find_class(class_name)
    if el:
        text = el[0].text_content().encode('utf-8').decode()
        return text.replace('\t', '').replace('\n', '')
    return ''


class GoodsNode:
    def __init__(self, el):
        self.el = el

    @property
    def _get_title(self):
        return get_text(self.el, 'g-i-tile-i-title')

    @property
    def _get_price(self):
        return get_text(self.el, 'g-price g-price-cheaper')

    def get_object(self):
        return {
            'title': self._get_title,
            'price': self._get_price
        }


class Page(object):
    URL_TEMPLATE = 'http://rozetka.com.ua/stabilizers/c144719/page=2/'

    def parse(self):
        content = request.urlopen(self.URL_TEMPLATE.format(1)).read()
        document = fromstring(content)
        for el in document.find_class('g-i-tile-i-box-desc'):
            node = GoodsNode(el)
            print(node.get_object())


def main():
    Page().parse()


if __name__ == '__main__':
    main()