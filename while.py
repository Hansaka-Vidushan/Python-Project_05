# While Loop

count = 0

while True:
    if count == 57:
        break
    print("Count: " + str(count))
    count += 1

print("""\n###########################################\n""")

# Continue using while loop
x = [1,2,3,4,5,6,7,8,9]

count = 0

while True:
    if count == len(x) -1:
        break
    a = x[count]
    if a % 2 == 0:
        count += 1
        continue
    print(a)
    count += 1