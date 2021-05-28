import random

# Card deck list

J = 10
Q = 10
K = 10
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]


# User inputs

start = input("Would you like to play Blackjack?")
if start == "Yes":
    name = input(str("What is your name?"))
    counter = int(input("How many counters do you want to play? Max number of counters are 2500"))
    if counter > 2500:
        counter = int(input("Can't have more than 2500, Please enter 2500 or under"))
else:
    print("Thank you for playing Blackjack")
    exit()

# Counter play

counterplay = int(input("How many counters do you want to play? Min counters is 100"))

# User cards

ucard1 = random.choice(cards)
ucard2 = random.choice(cards)
utotal = ucard1 + ucard2
print("Your first card is:", ucard1, "and your second card is:", ucard2, "with the total of:", utotal)
if utotal == 21:
    print("Blackjack!", name, "wins!")
    counter = counter - counterplay
# Computer cards

dcards1 = random.choice(cards)
dcards2 = random.choice(cards)
dtotal = dcards1 + dcards2
print("The dealer's first card is:", dcards1)

# Asks the user if they want to Hit, Stand or Double

uanswer = input(str("Would you like to Hit, Stand or Double?"))

# Hit Play

if uanswer == "Hit":
    ucard3 = random.choice(cards)
    utotal = utotal + ucard3
    if utotal == 21:
      print(name, "wins with the total of",utotal," with the 3rd card",ucard3)
      counter = counter - counterplay
    elif utotal != 22:
        print(utotal)
        uanswer2 = input("Would you like to Hit, Stand or Double?")
        if uanswer == "Hit":
            ucard4 = random.choice(cards)
            utotal = utotal + ucard4
            if utotal == 21:
                print(name, "wins with the total of",utotal,"! Their 4th card was",ucard4)
                counter = counter - counterplay
            elif uanswer2 == "Stand":
                print("The dealer has",dcards1, "and their second card is",dcards2,"and the total of",dtotal)
                if dtotal >= utotal + 1:
                    print("Dealer wins")
                elif dtotal <= utotal - 1:
                    print(name, "wins")
            elif utotal >= 22:
                print("Bust")
                counter = counter - counterplay
    elif utotal >= 22:
        print("Bust")
        counter = counter - counterplay
    else:
        exit()
    # Stand Play

elif uanswer == "Stand":
    print("The dealer has", dtotal)

# Double Play

elif uanswer == "Double":
    counterplay = counterplay * 2
    ucard3 = random.choice(cards)
    utotal = utotal + ucard3
    if utotal == 21:
        print(name, "wins with the total of",utotal,"with the third card",ucard3)
        counter = counter - counterplay
    elif utotal >= 22:
        print("Dealer wins with the total of",dtotal)
        counter = counter - counterplay
    elif utotal != 21:
        if dtotal <= utotal:
            print(name, "wins with the total of", utotal)
            counter = counter - counterplay
        elif dtotal == utotal:
            print("Draw!")
        else:
            print("You got", utotal, "and dealer wins with",dtotal)
            counter = counter - counterplay

# Prints counters left
print("You have",counter,"left!")
