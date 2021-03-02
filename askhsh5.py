import random
tmplist = []
tmplist2 = []
SOSlist = []

width = input("Give desired width:")
length = input("Give desired length:")

#checking if user gave integers
try:
    width = int(width)
    length = int(length)
except:
    print("Error. Exiting")
    exit()

#setting up for the 100 calculations
Averagecounter = 0
for k in range(100):
    #generating 1D list
    wholeseats = width * length
    for i in range(wholeseats):
        if i < wholeseats//2:
            tmplist.append('S')
        else:
            tmplist.append('O')


    #shuffling 1D list
    random.shuffle(tmplist)


    #appending 1D list objects to the 2D list
    tmpcounter = 0
    for i in range(width):
        tmplist2.clear()
        for j in range(length):
            tmplist2.append(tmplist[tmpcounter])
            tmpcounter = tmpcounter + 1
        SOSlist.append(tmplist2[:])

    SOScounter = 0
    #Searching for "SOS" in rows
    for i in range(width):
        for j in range(length-2):
            if (SOSlist[i][j] == "S") & (SOSlist[i][j+1] == "O") & (SOSlist[i][j+2] == "S"):
                SOScounter = SOScounter + 1

    #searching for "SOS" in columns
    for j in range(length):
        for i in range(width-2):
            if (SOSlist[i][j] == "S") & (SOSlist[i+1][j] == "O") & (SOSlist[i+2][j] == "S"):
                SOScounter = SOScounter + 1

    #searching for "SOS" diagonally (left to right) like this:
    # S
    #     O
    #         S
    for j in range(length-2):
        for i in range(width-2):
            if (SOSlist[i][j] == "S") & (SOSlist[i+1][j+1] == "O") & (SOSlist[i+2][j+2] == "S"):
                SOScounter = SOScounter + 1

    #searching for "SOS" diagonally (right to left) like this:
    #         S
    #     O
    # S
    for j in range(length-1, 2, -1):
        for i in range(width-2):
            if (SOSlist[i][j] == "S") & (SOSlist[i-1][j-1] == "O") & (SOSlist[i-2][j-2] == "S"):
                 SOScounter = SOScounter + 1


    Averagecounter = Averagecounter + SOScounter


#printing Output
AverageSosShowUps = Averagecounter/100
print("Average SOS formations:")
print(AverageSosShowUps)
