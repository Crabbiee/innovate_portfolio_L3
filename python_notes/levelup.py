import random
# # # int() - converts to integer
# # # float() - converts to floating point
# # # str() - converts to string
# # # type - tells you the type

# print(int(5.4))
# print(type(int("45"))) # - this prints what the value is, int, str etc

# balance = 100
# deposit = int(input("How much do you want to deposit"))
# balance +=deposit
# print(F"You have {balance}")

# print("What is your name?")
# name = input()  # blank = false, any input = true

# if name: # any data on input creates the variable name.
#     print(f"Welcome {name} to innovate!")
# else:  # no data in input = false
#     print("You didn't submit a name.")

# day ="Monday"
# bank_hol = None
# # anything other than a false value makes bank_hol true
# if day =="Saturday" or day=="Sunday" or bank_hol:
#     print("A day off!")
# else:
#     print("To work we go!")

# yes=["Gary","Chris","Bob","Laura","Claire"]
# name=input("What is your name?: ")
# while name not in yes:  # not in will see if the input is not in the list
#     print("You aren't on the list.")
#     print("Try again.")
#     name=input("What is your name?: ")
# print("You can come in")

# print("What coat is always wet when you put it on")
# answer=input("Answer: ")
# if "paint" in answer: # in is p much the opposite of not in
#     print("Correct")

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    try:
        print(int(num1) + int(num2))
    except:
        print("Enter a NUMBER only")
        add_up()
add_up()   #  TRY/EXCEPT WILL TRY TO DO SOMETHING, AND IF IT FAILS IT WILL RUN THE EXCEPT INSTEAD OF JUST HITTING A FATAL ERROR

# light = False

# def light_switch():
#     global light   # this makes the variable GLOBAL so that it can be updated and used globally
#     if light:
#         print("It's bright in here!")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True
# light_switch()
# light_switch()
# light_switch()
# light_switch()


# even_nums =[2,4,6,8,10]  # lists can be changed. remove,append, pop etc. lists = []
# even_nums.append(12)
# even_nums.insert(0,0)
# print(even_nums)

# odd_nums=(1,3,5,7,9)  # tuples CANNOT be changed. (IMMUTABLE). no remove, append etc tuples = ()
# # odd_nums.append(11) # - this wont work
# print(odd_nums)


# fav_games = [
#     "Final fantasy",
#     "Dark souls",
#     "Apex legends",
#     "Nioh"
# ]
# print(fav_games[1:2:1])  # [start:stop:step]
# print(fav_games[1]) # this is an index position - the start value.
# print(fav_games[1:2:3])  # starts at one, stops short of 2, steps by 1 at a time.


# #makes a string variable.
# #if it reads forwards the same as backwards
# # if it does, print YES. if it doesnt, print NO.

# test = "eggo"
# if test == test[::-1]:
#     print(f"Yes, {test} is a palindrome!")
# else:
#     print(f"{test} is not a palindrome.")



# num=random.randint(1,50)
# while num % 2 ==0:
#     print("Even number, again!")
#     num=random.randint(1,50)
# #odd number means the while loop will never run.
# print("Oh no! An odd number!")
# ###########################################

while True:
    num=random.randint(1,50)
    print(num)
    if num % 2 == 0:
        print("Even number, again!")
        continue
    else:
        print("Oh no, odd number!")
        break
#this while loop will always initalise, it might go straight to the end but it will have started