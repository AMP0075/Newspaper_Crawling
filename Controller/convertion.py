import pandas as pd
import os
def convert(articles, myfile, dateformat, rbuttonvar):
    masterkey=""

    if(len(articles)==0):
        return

    column=list(articles[0].keys())

    dataFrame = pd.DataFrame(articles,columns=column)

    for key,val in rbuttonvar.items():
        if val.get()==1:
            masterkey=key

    file=myfile+"."+masterkey

    if column.__contains__("Date"):
        dataFrame.Date=pd.to_datetime(dataFrame.Date,format=dateformat)

    if(os.path.exists(file)):
        if masterkey=="csv":
            original = pd.read_csv(file)
            res = original.append(dataFrame, ignore_index=True)
            res.to_csv(file, index=False, columns=column)
        elif masterkey=="xlsx":
            original = pd.read_excel(file)
            res = original.append(dataFrame, ignore_index=True)
            res.to_excel(file, index=False, columns=column)
        elif masterkey=="json":
            original = pd.read_json(file)
            res = original.append(dataFrame, ignore_index=True)
            res.to_json(file)

    else:

        if masterkey=="csv":
            dataFrame.to_csv(file, index=False, columns=column)
        elif masterkey=="xlsx":
            dataFrame.to_excel(file, index=False, columns=column)
        elif masterkey=="json":
            dataFrame.to_json(file)



