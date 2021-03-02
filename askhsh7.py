import urllib.request
import json
import datetime

#list declaration
frequentnumbers = []

for i in range(100):
    frequentnumbers.append(0)

#getting today's date
date = datetime.datetime.now()
#looping from 1st of the month to today
for i in range(1 , date.day+1):

    #Building date from 1st to today
    print("Working on date" , datetime.date(date.year, date.month, i) , "...")
    datetime.date(date.year, date.month, i)

    #Building url to request
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/"
    url = url + str(datetime.date(date.year, date.month, i))
    url = url + "/"
    url = url + str(datetime.date(date.year, date.month, i))
    url = url + "/"

    #Retrieving data
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)

    #processing for each draw
    for draw in data["content"]:
        t=draw["winningNumbers"]["list"]
        t.sort()
        # print("Calculating: " , t)

        #Adding +1 to the "frequentnumbers" list to the position of each number
        for inddraws in t:
            frequentnumbers[inddraws] = frequentnumbers[inddraws] + 1

#Finding max number
# print(frequentnumbers)
m = max(frequentnumbers)
counter = 0
print("here's the most frequent number(s):")
#Printing the position (the number that is) each time the number is show m times
#(since two numbers can have the same amount of show ups)
for i in frequentnumbers:
    if m == i :
        print(counter)
    counter = counter + 1
