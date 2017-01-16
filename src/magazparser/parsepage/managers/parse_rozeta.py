#!/usr/bin/python
#  -*- coding: utf-8 -*-

import requests
from lxml import html
import urllib.parse
import urllib.request
import smtplib


class Rozetka(object):

    REZULT = []
    """
    def parse_rozetka(self):

        url = 'http://rozetka.com.ua/stabilizers/c144719/'
        r = requests.get(url)
        res  = html.fromstring(r.content)
        result = res.xpath
    """

    def parse_rozetka(self):
        url = 'http://rozetka.com.ua/stabilizers/c144719/'
        r = requests.get(url)
        res  = html.fromstring(r.content)
        result = res.xpath
        return result


    def get_page_data(self,num):
        url = 'http://rozetka.com.ua/stabilizers/c144719/'
        for i in range(1,num):
            r = requests.get(url.format(i))
            self.get_all(r.content)
        return self.REZULT

    def get_all(self,data):
        data = self._get_desc(data)
        for key,i in enumerate(data):
              #href = i.xpath('//h3[@class="title item-description-title"]/a/@href')[key]
              href = i.xpath('//*[@class="g-i-tile-i-title clearfix"]/a/@href')[key]
              price = i.xpath('//*[@class="g-price-uah")@(text)')[key]
              self.REZULT.append({'href':'http://rozetka.com.ua/' + href,
                                  'price':price
                                  })

    def _get_desc(self, data):
        return self.get_from_xpath(data, '//div[@class="g-i-title-i avalilble"]')


    def get_from_xpath(self, data, xpath):
        res = html.fromstring(data)
        return res.xpath(xpath)

if __name__ == '__main__':
    rozetka = Rozetka()
    rozetka.parse_rozetka()
    msg = u'Subject: Stabilaizers'+"\n"
    for res in rozetka.REZULT:
        for k,i in res.items():
            msg+=str(res[k].strip()+"\n")
            msg+='-----------------------'+'\n'

    print(msg)

"""
if __name__ == '__main__':
    avito = Avito()
    avito.parse_avito_run()
    msg = u'Subject: Земельные участки'+"\n"

    for res in avito.RESULT:
        for k, i in res.items():
            msg+=str(res[k]).strip()+"\n"
        msg+='-------------------------------'+'\n'
    a = msg.sort()
    print(a)
"""