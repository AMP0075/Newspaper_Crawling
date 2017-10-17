from tkinter import *
from tkinter import messagebox
from Scrapper import ScrapToi
from Scrapper import scrapehinuarticle
from Covertion.convertion import convert
from datetime import datetime

def findArticles():


    if paperListBox.curselection().__contains__(0):
        to = ScrapToi.toi(baseurl="http://timesofindia.indiatimes.com/2016/11/23/archivelist/year-2016,month-11,starttime-",
                          keywords=getKeywords(), startdate=startDateEntry.get(),
                          enddate=endDateEntry.get(),attributes=myvar)
        print(to.articles)
        convert(to.articles, filename.get(), to.getDateFormat(), rbuttonvar)

    if paperListBox.curselection().__contains__(1):
        hindu = scrapehinuarticle.ScrapHindu(baseurl="http://www.thehindu.com/archive/web/",
                                             keywords=getKeywords(), startdate=startDateEntry.get(),
                                             enddate=endDateEntry.get(), attributes=myvar)
        print(hindu.articles)
        convert(hindu.articles, filename.get(), hindu.getDateFormat(), rbuttonvar)


def getKeywords():

    inputlist=searchTermEntry.get().split(',')
    inputlist2=[]
    for i in inputlist:
        inputlist2.append(i)
        inputlist2.append(i.upper())
        inputlist2.append(i.capitalize())
    return inputlist2

def validateDate(datestring):
    try:
        datetime.strptime(datestring, '%Y-%m-%d')
    except ValueError:
        return 0
    return 1

def validate():
    if validateDate(startDateEntry.get()) and validateDate(endDateEntry.get()):
        findArticles()
    else:

        messagebox.showerror("Invalid Date","Please enter a valid date")


top=Tk()
labels=["Date","Heading","Article","Category","Paper","Link","City"]
formatlabels=["csv","json","xlsx"]
rbuttonvar={}
myvar={}


labelText=StringVar()
labelText.set("Enter Keywords")
labelDir=Label(top, textvariable=labelText)
labelDir.pack()
searchTermEntry=Entry(top,bd=5)
searchTermEntry.pack()

labelText1=StringVar()
labelText1.set("Enter Start Date Format- YYYY-MM-DD")
labelDir1=Label(top, textvariable=labelText1)
labelDir1.pack()
startDateEntry=Entry(top)
startDateEntry.pack()


labelText2=StringVar()
labelText2.set("Enter End Date Format- YYYY-MM-DD")
labelDir2=Label(top, textvariable=labelText2)
labelDir2.pack()
endDateEntry=Entry(top)
endDateEntry.pack()

labelText6=StringVar()
labelText6.set("Select Newspapers")
labelDir6=Label(top, textvariable=labelText6)
labelDir6.pack()
paperListBox=Listbox(top,selectmode=MULTIPLE,height=3)
paperListBox.insert(1,"Times Of India")
paperListBox.insert(2,"The Hindu")
paperListBox.pack()


labelText3=StringVar()
labelText3.set("Select Attributes")
labelDir3=Label(top, textvariable=labelText3)
labelDir3.pack()
for i in range(len(labels)):
    var = IntVar()
    myvar[labels[i]] = var
    C=Checkbutton(top,text=labels[i],variable=myvar[labels[i]], \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
    C.pack()


labelText4=StringVar()
labelText4.set("Select Output Format")
labelDir4=Label(top, textvariable=labelText4)
labelDir4.pack()
for i in range(len(formatlabels)):
    var=IntVar()
    rbuttonvar[formatlabels[i]]=var
    r=Radiobutton(top,text=formatlabels[i],variable=rbuttonvar[formatlabels[i]],value=1)
    r.pack()


labelText5=StringVar()
labelText5.set("Enter Filename")
labelDir5=Label(top, textvariable=labelText5)
labelDir5.pack()
filename=Entry(top)
filename.pack()

findButton=Button(top, text="Find Articles", command=validate)
findButton.pack()


top.mainloop()