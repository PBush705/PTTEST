import random
#Define Total
count = 0

#We store our lives here. Default Value is 5.
life = 5

#We use 'list' in order to categorize the different words
lst = ['Plants', 'Trees', 'Luck', "Tough",
        "Increasing", "Delusional", "Dinosaur", "velociraptor"]

#This is the difficulty option, Normal Mode is a regular easier list
#If Normal is false, it will go into hard mode with a 30 second timer.
normal = True

test = " "

#Retry Function
def retry():
    global life
    life = 5
    retry = input("Would you like to try again? (Y/N) ")
    if retry == "yes" or retry == "Yes" or retry == "YES" or retry == "Y" or retry == "y":
        answer = random.choice(lst)
        guess(answer)
    elif retry == "no" or retry == "No" or retry == "NO" or retry == "N" or retry == "n" or retry == "":
        quit()
#Function to Guess the Word
def guess(arg):
    count = 0
    print("Guess the Word")
    #Use this function to count the number of letters
    yes = arg
    print(yes)
    for i in yes:
        count = count + 1    
    no = ("-" * count)
    
    for x in arg:
        global test
        for i in test:
            if i == x:
                cool = arg.index(i)
                no.replace(no[cool], arg[cool])
    print(str(count) + " " "letters")
    print(no)
    test = input()
    if test == arg:
        print("""You Got it!
                           ____
                  _           |---||            _
                  ||__________|SSt||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    '''''           ''-         ''-         ''-         '''  '''

""")
        retry()
    
    elif test != arg:
        print("You missed!")
        print("The answer is" + " " + test)
        for i in test:
            print(i)
            print(no)
        if test == int:
            print("There are no numbers :)")
        global life
        life -= 1
        print(life)
        if test != arg and life == 0:
            print("""Game Over!
            /`-.
                    .-/   /
                    `._`./.
                _ /oo`..'_
        ._    __(-|  =-| _ )
        ,-;==== _ - ,.  _-(    __
            `   (  --_ -_  =====:-.`
            `._________,'   `""")
            retry()
        save1 = answer 
        guess(save1)
        




#Choose a random string from the list
answer = random.choice(lst)

guess(answer)