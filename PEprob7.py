#This algorithm is designed to find the 10001st prime number. It will use two functions, main and isprime
def isprime(number):
    internalcounter = 2
    while internalcounter < number:
        if number % internalcounter == 0:
            return False
        internalcounter = internalcounter + 1
    return True
def main():
    primecounter = 0
    overallcounter = 0
    while primecounter < 10002:
        overallcounter += 1
        if isprime(overallcounter):
            primecounter += 1
    print(overallcounter)
main()