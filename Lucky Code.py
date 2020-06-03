import csv
import random as r
import time as t

print("Welcome to Raffle 4.0 Lucky Draw")
print("Created by Shashi")


def lucky_draw2():
    file1 = open("raffle.csv", 'r')
    file = csv.reader(file1)
    mylist = list(file)
    m = len(mylist)
    winner_list = []

    n = int(input("Enter the number of winner you want / Number of lucky draw you want to perform: "))
    k=0
    while k<n:

        num = r.randint(0,m-1)
        if num in winner_list:
            pass
        else:
            winner_list.append(num)
            print("Lucky draw number =", k + 1)
            print("Ticket Number", mylist[num][0], "won.")
            k+=1
            t.sleep(1)


    print("")
    print("Loading winner's details.")
    t.sleep(0.5)
    print("Loading winner's details...")
    t.sleep(1)
    print("Loading winner's details.....")
    t.sleep(1)
    print("Loading winner's details.......")
    print("")
    print("Winner's details: ")
    print("")
    #print(f"S.No  {' '.join(mylist[0])}")
    j = 1
    for i in winner_list:
        print(f"{j}   : {' '.join(mylist[i])}")
        j += 1
        #time delay winner
        t.sleep(2)
    print("")
    print("Cogratulation to all winners!!!")
    file1.close()

lucky_draw2()





