def greet(name) :
    print("Hello " + name)

def user_input() :
    return input("Please enter your name")






def language_input():
    print("1:English")
    print("2:Kannada")
    print("3:Hindi")
    language = input("Please select number 1, 2,3 for diff langauages ")
    print (language)
    if language == 1:
        print("You have choosen English")
    elif language == 2:
        print("You have choosen Kannada")
    else:
        print ("you have choosen Hindi")
    greet(user_input())

language_input()