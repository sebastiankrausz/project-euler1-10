import math
count = 0
i = 1
while i < 1000:
    if i % 3 == 0:
        count = count + i
        i += 1
    elif i % 5 == 0:
        count = count + i
        i += 1
    else:
        i += 1
print(count)
