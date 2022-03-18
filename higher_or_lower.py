from random import randrange

def askUserNumber():
    input("Please enter number between 0 to 10")

uNum=askUserNumber()
def returnRandomNum1_10():
    return randrange(10)

numRandom=returnRandomNum1_10()
def  evaluatesNum():
    if askUserNumber() > returnRandomNum1_10() :
        print("User guess is too high")
    elif askUserNumber() < returnRandomNum1_10() :
        print ("User guess is too low")
    else  :                       #askUserNumber()==returnRandomNum1_10()
        print ("your guess is correct")
    print("User Guess"+str(uNum))
    print("Random Number"+str(numRandom))

evaluatesNum()