import urllib
import json
import requests
import time
import matplotlib.pyplot as plt

ploter=[]
plt.show()
ploter1=[]
eu2=[]
i=0
while True:
    f=open("BTCval.txt","a+")
    plt.ylabel("BTC value in €")
    response=urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json")
    rawValue=response.read()
    value=json.loads(rawValue)
    newVal=value['bpi']
    Euro=newVal['EUR']
    print("Current BTC value is: ",Euro['rate'],"€")
    time.sleep(0.3)
    eur=Euro['rate']   
    ploter.append(eur)
    e=ploter[i].replace(',','')
    eu=float(e)
    print(eu)
    eu2.append(eu)
    ts=value['time']
    ts1=ts['updated']
    f.write("%f"%eu)
    f.write("%s \n"%ts1)
    plt.plot(eu2)
    plt.pause(0.01)
    plt.clf()
    plt.draw()
    i+=1
f.close()