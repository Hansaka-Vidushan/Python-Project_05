x = [1,2,3,4,5,6,7,8,9]

# Find Total
total = int()

for tot in x:
    total += tot
print("Total: " , total)

# Find average
print("Average: " , total/len(x))

# Find Max
Max = x[0]

for max in x:
    if Max < max:
        Max = max
print("Max: ", Max)

# Find Min
Min = x[0]

for min in x:
    if Min > min:
        Min = min
print("Min: " , Min)






