#PEproblem10: Summation of primes. The task is simple, find the sum of all primes below two million. I will be borrowing my isprime
#function which I wrote for problem three. Then I will have an overall counter that works upward to two million.
def isprime(number):
    internalcounter = 2
    while internalcounter < number:
        if number % internalcounter == 0:
            return False
        internalcounter = internalcounter + 1
    return True
summation_of_primes = 2
counter = 3
while counter < 2000000:
    if isprime(counter) == True:
        summation_of_primes = summation_of_primes + counter
        counter += 1
print(summation_of_primes)