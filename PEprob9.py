
#Project Euler Problem 9.
#The goal of this problem is to find the pythagorean triplet a^2 + b^2 = c^2, for which a + b + c = 1000
#more specifically to find the multiple a * b * c.
#I propose a main function with two for loops that iterate over pre-created lists of potential a and b values
#There will be two user-defined functions, is_special_triplet, which will be passed a and b and decide if the triplet is special. If it is, it will multiply the three values
def is_special_case(a,b,c):
    if a + b + c == 1000:
        return True
def generate_list():
    counter = 0
    new_list = []
    while counter < 450:
        new_list.append(counter)
        counter = counter + 1
    return new_list
def main():
    alist = generate_list()
    blist = generate_list()
    for a in alist:
        for b in blist:
            c = (a ** 2 + b ** 2) ** 0.5
            if is_special_case(a,b,c) == True:
                print (a*b*c)
            
main()    
        

    
