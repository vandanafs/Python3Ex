from random import randrange

def ask_user_number():
     userGuess=  input("Please enter number between 0 to 10")
     return userGuess


guess=ask_user_number()
def return_random_num1_10():
    return randrange(10)

numRandom=return_random_num1_10()


def  evaluatesNum():

   #userGuess = input("Please enter number between 0 to 10")
   if  guess> return_random_num1_10() :
        print("User guess is too high")
   elif guess < return_random_num1_10() :
        print ("your  guess is too low")
   else  :                       #askUserNumber()==returnRandomNum1_10()
        print ("your guess is correct")
   print("User Guess"+str(guess))
   print("Random Number"+str(numRandom))

evaluatesNum()