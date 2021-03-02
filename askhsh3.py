import urllib.request
import json
import datetime

date = datetime.datetime.now()
for i in range(1 , date.day+1):
    datetime.date(date.year, date.month, i)
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/"
    url = url + str(datetime.date(date.year, date.month, i))
    url = url + "/"
    url = url + str(datetime.date(date.year, date.month, i))
    url = url + "/"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)
    draw = data["content"][0]
    t = draw["winningNumbers"]["list"]
    print("Oi arithmoi pou kerdizoun stis", datetime.date(date.year, date.month, i) , "einai:")
    print(t)
