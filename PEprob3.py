counter = 1
multiple = 600851475143
#I want there to be two functions. One function, isfactor, will determine if a number is a factor of
#600851475143. A second funciton will determine if the number is prime. The main function will print all number that are prime factors
#
def isprime(number):
    internalcounter = 2
    while internalcounter < number:
        if number % internalcounter == 0:
            return False
        internalcounter = internalcounter + 1
    return True
def isfactor(number):
    if 600851475143 % number == 0:
        return True
    else:
        return False
while counter < 600851475143:
    if isprime(counter) == True and isfactor(counter) == True:
      print(counter)
    counter += 1
    
    
