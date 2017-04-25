import re

import bs4
import requests
from datetime import datetime,timedelta
from Model.ScrapAbstract import ScrapAbstract


class ScrapHindu(ScrapAbstract):
    def __init__(self,baseurl,keywords,startdate,enddate,attributes):
        super(ScrapHindu,self).__init__(baseurl,keywords,startdate,enddate,attributes)

    def getArticle(self, soup,link):
        div = soup.find_all("div", id=re.compile(r'content-body-.*'))
        for d in div:
            paralist = d.find_all("p")
        paralist2 = []
        for p in paralist:
            paralist2.append(p.getText())

        combparalist = ("\n").join(paralist2)
        return combparalist


    def getPaper(self, soup,link):
        return "The Hindu"


    def getHeading(self, soup,link):
        head = soup.find_all("h1", class_='title')
        if (len(head) > 0):
            return head[0].getText().replace('\n', '')


    def getDate(self, soup,link):
        date = soup.find_all("none", string=re.compile(r'(IST)'))
        if (len(date) > 0):
            return date[0].getText()


    def getCategory(self, soup, link):
        cat = soup.find_all("a", class_='section-name')
        if (len(cat) > 0):
            return cat[0].getText().replace('\n', '')


    def getLink(self, soup, link):
        return link


    def getCity(self, soup, link):
        return soup.find_all("span",class_='blue-color ksl-time-stamp')[0].getText().replace('\n','').replace(':','')


    def getLinks(self):

        d1 = datetime.strptime(self.startdate, "%Y-%m-%d")
        d2 = datetime.strptime(self.enddate, "%Y-%m-%d")

        while d1!=d2:

            try:
                r = requests.get(self.baseurl+str(d1.year)+"/"+str(d1.month)+"/"+str(d1.day))
            except requests.exceptions.Timeout:
                print("timeout")
            except requests.exceptions.TooManyRedirects:
                print("Bad url")
            except requests.exceptions.RequestException as e:
                print(e)


            soup = bs4.BeautifulSoup(r.text, "lxml")
            a = soup.find_all(class_="archive-list")
            print(d1)
            for li in a:
                listlinks = li.find_all("a", string=re.compile(r'('+self.keywordstring+')'))
                for l in listlinks:
                    self.q.put(l['href'])

            d1 = d1 + timedelta(days=1)

    def getDateFormat(self):
        return "\n%B %d, %Y %H:%M %Z\n"
