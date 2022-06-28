import random

greeting = "Hello world"
print(f"This is a variable > {greeting}")

print(greeting.lower())
print(f"There are {len(greeting) - greeting.count(' ')} characters in \"{greeting}\"")

print("This is a string for displaying characters")
print("1234") #this is a string
print(1234+1) #this is an integer/whole number
print(12.34) #this is a float
print(True) #one of the boolean data values
print(False) #one of the boolenans
print(None) # blank/null/no data

print(len(greeting))
print(greeting[1])
print(greeting[-1])

print("HELLO".lower())
print("hello EVERYONE".capitalize())
print("This quick brown fox fox fox".count("fox"))
print("the quick brown fox".find("T"))
print("The quick brown fox".replace("fox", "egg"))
print("The quick brown fox".strip()) 
print("The quick brown fox".strip("fox")) #The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

print(random.random())  #random floating point number
print(random.uniform(1,10)) #random floating point between (x,y)
print(random.randint(1,10)) #random integer between (x,y)

my_name="Dodongo"
my_age=93
student=False
print(my_name)
print("My name is " + my_name)
#print(f"I am" + my_age) #this one breaks, is no good.

print("Bonjour call me {} and know that i am {} years old.".format(my_name,my_age))  #.format() used to be the way, {} as placeholder then put variables in ()

print(f"Ello i'm {my_name} and i'm only {my_age}.") # f string best practice, very smooth, very nice.


# print(1+2)
# print(3-2)
# print(3*3)
# print(3**3)
# print(6/2)
# print(15%3)

# balance=100
# amount=20

# balance=amount+balance
# balance =+ amount
# print(balance)

answer = input("What is your name? \n").strip()
print(f"{answer.capitalize()}? Weird.")
# the answer variable becomes whatever is defined via input

music = "jazz"
if music == "jazz":
    print("Jazz is whack")
elif music == "no music":
    print("Ah silence.")
else:
    print("Good choice.")
#if statements

print (10%2==0)

num=10
num2=20
if num > num2:
    print(f"{num} is bigger.")
elif num2 > num:
    print(f"{num2} is bigger")
else:
    print("They are equal")

place ="MCR"
weather ="raining"

if place =="MCR" and weather =="sunny":
    print("sun? lol whatever")
elif place =="MCR" and weather =="cloudy":
    print("ooh cloudy")
else:
    print("Of course its raining")
#if statement with and operator

day = "monday"
bhol = True
if day =="Saturday" or day=="Sunday" or bhol:
    print("It's your day off. go have fun!")
else:
    print("Time to grind")
# if statement with or operator and boolean


def cash_wdraw(amount,accnum):
    print(f"You have withdrawn £{amount} from account number {accnum}")
cash_wdraw(300, 55773399)
# defined and then called function


fav_games = [
    "Final fantasy",
    "Dark souls",
    "Apex legends"
]
print(fav_games)
fav_games[1] = "GTA" #changes the second list item to GTA
print(fav_games)
print(len(fav_games))
fav_games.append("Metal gear solid") #adds to the end of list
print(fav_games)
fav_games.pop(2)
print(fav_games)
#various list functions