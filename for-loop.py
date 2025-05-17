# Loops

# For Loop
x = [2,3,4,5,6,7,8]
index = 0

# Method 01
for Element in x:
    y = x[index]
    print(index , y)
    index += 1


# Method 02
for index , value in enumerate(x):
    print(index , value)


z = [2,3,4,5,6]

for item in range(0,2):
    print(item)

print("""###############################################################

""")

# Continue Using For Loop
x = [1,34,56,43,76,56,87]

for a in x:
    if a % 2 == 0:
        continue
    print(a)


print("####################################################################\n")

# Dictionary Iterate
x = {
    "Hansaka": 19,
    "Sathmina": 16,
    "Senehas": 14,
    "Vihanga": 12

}

for name , age in x.items():
    print(name , age)


print("####################################################################\n")


# Tuple Iterate

x = ("Hansaka" , 12, "Sathmina" , 90 , 76)

for tup in x:
    print(tup)

print("####################################################################\n")


# Set Iterate
x = {"hansaka" , 10 , 86}

for set in x:
    print(set)
