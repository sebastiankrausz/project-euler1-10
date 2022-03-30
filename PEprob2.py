import math
summation = 0
counterold = 1
counternew = 2
def update_sequence(counterold, counternew):
    storageval = counterold
    counterold = counternew
    counternew = storageval + counternew
    return (counterold, counternew)
while counternew <= 4000000:
    if counternew % 2 == 0:
        summation = summation + counternew
    [counterold, counternew] = update_sequence(counterold, counternew)
print(summation)
        
