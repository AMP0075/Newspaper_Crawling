import re

import bs4
import requests

from Scrapper.ScrapAbstract import ScrapAbstract
from datetime import datetime

class toi(ScrapAbstract):


    def __init__(self,baseurl,keywords,startdate,enddate,attributes):
        print(keywords,startdate,enddate)
        super(toi,self).__init__(baseurl,keywords,startdate,enddate,attributes)

    def getArticle(self, soup,link):
        div = soup.find_all("div", class_="Normal")
        if (len(div) > 0):
            return div[0].getText().strip().replace('\n', '')
        else:
            return ""

    def getPaper(self, soup,link):
        return "toi"



    def getHeading(self, soup,link):
        heading = soup.find_all("h1", class_="heading1")
        if (len(heading) > 0):
            return heading[0].getText()

    def getDate(self, soup,link):
        date = soup.find_all("span", string=re.compile(r'(IST)'))
        if (len(date) > 0):
            return date[0].getText().replace("Updated: ", "").replace('.', ':')

    def getCategory(self, soup, link):
        linkatrr = link.split('/')
        return linkatrr[4]

    def getCity(self, soup, link):
        linkatrr = link.split('/')
        if linkatrr[4] == 'city':
            return linkatrr[5]
        else:
            return ""

    def getLink(self, soup, link):
        return link

    def getLinks(self):
        startno,freq=self.days_between()
        print(self.baseurl+str(startno)+".cms",startno,freq)
        for i in range(freq):

            try:
                r = requests.get(self.baseurl+str(startno+i)+".cms")
            except requests.exceptions.Timeout:
                print("timeout")
            except requests.exceptions.TooManyRedirects:
                print("Bad url")
            except requests.exceptions.RequestException as e:
                print(e)

            soup = bs4.BeautifulSoup(r.text,"lxml")
            links = soup.find_all("a", string=re.compile(r'('+self.keywordstring+')'))
            print(links,i)
            for l in links:
                p=l['href']
                if "timesofindia.indiatimes.com" not in l['href']:
                    p="http://timesofindia.indiatimes.com"+l['href']
                self.q.put(p)

    def days_between(self):
        d0=datetime(2001,1,1)
        d1 = datetime.strptime(self.startdate, "%Y-%m-%d")
        d2 = datetime.strptime(self.enddate, "%Y-%m-%d")
        #36893
        return abs((d1 - d0).days)+36892,abs((d2 - d1).days)


    def getDateFormat(self):
        return "%b %d, %Y, %I:%M %p %Z"

