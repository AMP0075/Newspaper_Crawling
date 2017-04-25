from abc import ABC,abstractmethod
from queue import Queue
from time import time
from threading import Thread
import bs4
import requests

class ScrapAbstract(ABC):
    def __init__(self,baseurl,keywords,startdate,enddate,attributes):
        self.baseurl=baseurl
        self.articles=[]        #dictionary containing article atrributes
        self.q=Queue()
        self.keywordstring='|'.join(keywords)
        self.startdate=startdate
        self.enddate=enddate
        self.attributes = attributes
        self.grabData()



    @abstractmethod
    def getDate(self,soup,link):
        pass

    @abstractmethod
    def getArticle(self,soup,link):
        pass

    @abstractmethod
    def getHeading(self,soup,link):
        pass

    @abstractmethod
    def getPaper(self,soup,link):
        pass


    @abstractmethod
    def getLink(self,soup,link):
        pass

    @abstractmethod
    def getCategory(self,soup,link):
        pass

    @abstractmethod
    def getCity(self,soup,link):
        pass

    @abstractmethod
    def getDateFormat(self):
        pass

    @abstractmethod
    def getLinks(self):
        pass


    def extractData(self,link):
        dispatcher={"Date":self.getDate,"Article":self.getArticle,"Paper":self.getPaper,"Heading":self.getHeading,"Link":self.getLink,"Category":self.getCategory,"City":self.getCity}
        attr = {}

        try:
            r = requests.get(link)
        except requests.exceptions.Timeout:
            print("timeout")
        except requests.exceptions.TooManyRedirects:
            print("Bad url")
        except requests.exceptions.RequestException as e:
            print(e)

        soup = bs4.BeautifulSoup(r.text, "lxml")

        for key,value in self.attributes.items():
            if value.get()==1:
                attr[key]=dispatcher[key](soup,link)
        return attr



    def parseLinks(self,i):
        while True:
            print('thread {} running'.format(i))
            link = self.q.get()
            print(link)
            d=self.extractData(link)
            self.articles.append(d)
            self.q.task_done()

    def grabData(self):
        ts = time()
        for i in range(4):
            t1 = Thread(target=self.parseLinks, args=(i,))
            t1.setDaemon(True)
            t1.start()
        self.getLinks()
        self.q.join()
        print('grabdata took {}'.format(time() - ts))



