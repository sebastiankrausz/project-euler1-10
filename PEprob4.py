# PE problem 4 : Largest palindrome product.
# functions:
#reverselist, which reverses the list without actually altering the original list
#check_palindrome, which checks if a product is a palindrome
#generate_three_dig_list, which generates a list of all the three digit numbers
#then, there is the hardcoded section, which multiplies the two lists together and finds the largest palindrome that results from this multiplication
def reverselist(the_list):
    new_list = the_list[:]
    new_list.reverse()
    return new_list
def check_palindrome(product):
    #This function checks if a product is a palindrome
    list_of_product = [int(a) for a in str(product)]
    inverse_list_of_product = reverselist(list_of_product)
    if list_of_product == inverse_list_of_product:
        return True
    else:
        return False
def generate_three_dig_list():
    counter = 100
    three_dig_list = []
    while counter < 1000:
        three_dig_list.append(counter)
        counter = counter + 1
    return three_dig_list
multiple_list = generate_three_dig_list()
multiple_list2 = generate_three_dig_list()
biggest_palindrome = 1001
for number in multiple_list2:
    for item in multiple_list:
        product = item * number
        true_false = check_palindrome(product)
        if true_false == True:
            if product > biggest_palindrome:          
                biggest_palindrome = product
print(biggest_palindrome)
        



