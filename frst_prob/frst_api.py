import pymongo
from pymongo import MongoClient
import numpy as np
from pprint import pprint

client = MongoClient('mongodb+srv://backendconcoxdeveloper:V3jUV7QXqEoAtnhy@cluster0-zhjde.mongodb.net')
db = client['__CONCOX__']
d1 = db['devices']
d2 = db['status']

req_d1 = d1.find().limit(30)



class collected_data():
    def __init__(self,myquery):
        self.myquery=myquery
        self.mydoc = d2.find(self.myquery).limit(50)
        self.lst=[]
        for dta in self.mydoc:
            self.lst.append(dta['gps'])
            
def final_values():
    adrs=[]
    i=0
    for ele in req_d1:
        y=ele['id']
        z=y[1:5]
        adrs.append(None)
        myquery={'case' : z}
        #print(myquery)
        adrs[i]=collected_data(myquery)
        i=i+1

    return adrs

