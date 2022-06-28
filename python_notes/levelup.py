# # int() - converts to integer
# # float() - converts to floating point
# # str() - converts to string
# # type - tells you the type

print(int(5.4))
print(type(int("45"))) # - this prints what the value is, int, str etc

balance = 100
deposit = int(input("How much do you want to deposit"))
balance +=deposit
print(F"You have {balance}")

print("What is your name?")
name = input()  # blank = false, any input = true

if name: # any data on input creates the variable name.
    print(f"Welcome {name} to innovate!")
else:  # no data in input = false
    print("You didn't submit a name.")

day ="Monday"
bank_hol = None
# anything other than a false value makes bank_hol true
if day =="Saturday" or day=="Sunday" or bank_hol:
    print("A day off!")
else:
    print("To work we go!")

yes=["Gary","Chris","Bob","Laura","Claire"]
name=input("What is your name?: ")
while name not in yes:  # not in will see if the input is not in the list
    print("You aren't on the list.")
    print("Try again.")
    name=input("What is your name?: ")
print("You can come in")

print("What coat is always wet when you put it on")
answer=input("Answer: ")
if "paint" in answer: # in is p much the opposite of not in
    print("Correct")

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    try:
        print(int(num1) + int(num2))
    except:
        print("Enter a NUMBER only")
        add_up()
add_up()   #  TRY/EXCEPT WILL TRY TO DO SOMETHING, AND IF IT FAILS IT WILL RUN THE EXCEPT INSTEAD OF JUST HITTING A FATAL ERROR
