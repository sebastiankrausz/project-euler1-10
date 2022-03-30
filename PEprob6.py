#This algorithm will employ three defined functions, sumofsquares, squareofsum, and a final subtraction of the two.
def sumofsquares():
    counter = 1
    total = 0
    while counter < 101:
        total = total + counter * counter
        counter = counter + 1
    return total
def squareofsum():
    counter = 1
    pretotal = 0
    while counter < 101:
        pretotal = pretotal + counter
        counter = counter + 1
    return pretotal * pretotal
lil_sum = sumofsquares()
big_sum = squareofsum()
print(big_sum - lil_sum)