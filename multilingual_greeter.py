def greet(name) :
    print("Hello " + name)

def user_input() :
    return input("Please enter your name")






def language_input():
    print("1:English")
    print("2:Kannada")
    print("3:Hindi")
    language = input("Please select number 1, 2,3 for diff langauages ")

    if language == '1':
        print("You have choosen English")
        greet(user_input())
    elif language == '2':
        print("Neevu kannada bhase aayke madidira ")
        kannada= input("Nimma hesaru type maadi")
        print("Namaste "+kannada )
    else:
        print ("Aap hindi bhashe select kiya hai!")
        hindi=input("Aap naam type kijiye")
        print(f"Namaste {hindi}")
language_input()