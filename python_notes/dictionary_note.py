# # - DICTIONARIES DO NOT HAVE A NUMBERED INDEX
print("This be dictionaries")

my_pc = {
    "name":"Buscutte",
    "specs":"High",
    "draw":"Low"
}
print(my_pc["specs"])
my_pc["specs"] = "Low" # # - THIS UPDATES THE VALUE
print(my_pc["specs"])

pc_keys=my_pc.keys()
print(pc_keys)
print(my_pc.values())
print(my_pc.items())


print(list(my_pc.keys()))  #  - CONVERTS DICTIONARY INTO A LIST

for every_key in my_pc.keys():
    print(every_key)
my_pc.update({"colour":"Black"})
my_pc.update({"loved":"Yes"})
print(my_pc)
# # - UPDATE WILL ADD ITEMS TO THE DICTIONARY

my_pc.pop("loved")
print(my_pc)  # # THIS WILL REMOVE THE LOVED KEY/VALUE PAIR