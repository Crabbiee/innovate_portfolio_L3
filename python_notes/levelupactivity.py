def varint():
    num = input("Please input a number. \n")
    try:
        print(f"Success! {int(num)} has been converted into {type(int(num))}")
    except:
        print("Try again.")
        varint()

varint()
