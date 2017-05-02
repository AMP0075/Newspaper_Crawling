import requests,bs4,re
from datetime import datetime,timedelta
'''
keywords=["Demonet","demonet"]
arg = '|'.join(keywords)

soup = bs4.BeautifulSoup(requests.get("http://www.thehindu.com/todays-paper/Note-ban-relief-partly-withdrawn/article16739625.ece").text)
div = soup.find_all("span",class_='blue-color ksl-time-stamp')[0].getText()
#div1 = soup.find_all("h1",class_='title')

#div = soup.find_all("none",string=re.compile(r'(IST)'))[0].getText()

if "timesofindia.indiatimes.com" in "http://timesofindia.indiatimes.com/2016/11/23/archivelist/year-2016,month-11,starttime-":
    print("jai mata di")


print(div)


def days_between():
    d0 = datetime(2001, 1, 1)
    d1 = datetime.strptime(startdate, "%Y-%m-%d")
    d2 = datetime.strptime(enddate, "%Y-%m-%d")
    # 36893
    return abs((d1 - d0).days) + 36892, abs((d2 - d1).days)

startdate="2016-11-08"
enddate="2016-11-10"

startno,freq=days_between()

print('|'.join(['Congress']))

def manu():
    print("manu")

def anu():
    print("anu")

dispatcher={"manu":manu,"anu":anu}
attr={"manu":1,"anu":1}
for key,value in attr.items():
    if value==1:
        dispatcher[key]()



d1=datetime.strptime("2017-03-16","%Y-%m-%d")
d2=datetime.strptime("2017-04-02","%Y-%m-%d")

while d1!=d2:
    d1=d1+timedelta(days=1)
    print("http://www.thehindu.com/archive/web/"+str(d1.year)+"/"+str(d1.month)+"/"+str(d1.day))


column=["Date"]
if column.__contains__("Date"):
    print("Hello")


def validateDate(datestring):
    try:
        datetime.strptime(datestring, '%Y-%m-%d')
    except ValueError:
        print("galat hai")

'''
var="http://timesofindia.indiatimes.com//city/raipur/demonetisation-a-step-towards-more-transparent-economy-says-chhattisgarh-cm/articleshow/56419054.cms"
print(var.split('/'))




