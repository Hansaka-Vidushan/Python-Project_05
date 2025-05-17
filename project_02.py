x = [1,2,3,4,5,6,7,8,9]

count = 0
total = 0
average = 0
max = x[0]
min = x[0]

while count < len(x):
    # Get Total
    total += x[count]


    # Get Average
    average = total/len(x)

    # Get max
    if max < x[count]:
        max = x[count]

    # Get Min

    if min > x[count]:
        min = x[count]

    count += 1

print(total)
print(average)
print(max)
print(min)

