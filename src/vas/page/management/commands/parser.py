#!/usr/bin/env python3
import logging
from urllib import request
from lxml import html
import urllib
from django.core.management.base import BaseCommand
from django.db import models
from page.models import Apartment


logging.basicConfig(level=logging.DEBUG)

class ApartmentData(object):
    def __init__(self, node):
        self.node = node

    def _title(self):
        if self.node is None:
            return ''
        return self.node.text_content().encode('utf-8').decode()

    def _link(self):
        try:
            link = self.node.findall('a')[0].attrib.get('href', '')
            return 'https://vashmagazin.ua{}'.format(link)
        except IndexError:
            return ''

    @property
    def data(self):
        return Apartment(
            title=self._title(),
            link=self._link()
        )

class Page(object):

    HOST = 'https://vashmagazin.ua/nerukhomist/kvartyry/?item_price1=&item_price2=&page={}'

    def __init__(self, number):
        self.number = number

    @property
    def _url(self):
        return self.HOST.format(self.number)

    def parse(self):
        logging.info('Get page: {}'.format(self._url))
        response = request.urlopen(self._url).read()
        content = html.fromstring(response)
        return [ApartmentData(node).data for node in content.find_class('ner_h3')]


class Parser(object):
    PAGES_COUNT = 136

    def results(self):
        results = []
        for page_number in range(1, self.PAGES_COUNT):
            page = Page(page_number)
            results += page.parse()
        return results
    
class Command(BaseCommand):
    
    def handle(self,*args, **kwargs):
        Apartment.objects.bulk_create(Parser().results())