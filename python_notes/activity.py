##activity 1
# create a variable that holds the text "Welcome to code nation". Find the length of the string and save this to a new variable
#create a function that checks if the string length is even, if it is, print the string, the length and an appropriate message in one sentence. Do the same but with a diff message if its odd.

# text = "Welcome to code nation"

# def check():
#     length = len(text)
#     if (length % 2) == 0:
#         print("There are an even number of characters in this string")
#     else:
#         print("There are an odd number of characters in this string.")
# check()

#change the string length so you can test all possible outcomes.


##activity 2

abet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

for x in abet:
    print(x)
print("Enter a number from 1 - 26")
num = int((input()))
print(f"{num} represents the letter {abet[num - 1]} in the alphabet")
