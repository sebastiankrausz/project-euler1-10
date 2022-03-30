#PE problem 5: smallest multiple, the goal is to find the smallest number that can be evenly divided by the numbers 1-20. The initial idea is to have a
#local counter that continuously counts upward within a main function, and does not stop counting until the remainder of mod division by every number from 1 to 20
# is zero by way of a for loop.
# This is not the idea that was used, a weird counter was used instead.
#The moral of the story is that you should modfiy the counter before the condition is checked and the while loop is ended
#If you do not, an additional 20 will be tacked onto your answer, like happened here.
def main():
    factor_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    main_counter = 0
    condition = False
    while condition == False:
        little_count = 20
        main_counter = main_counter + 20
        for factor in factor_list:
            if main_counter % factor == 0:
                little_count = little_count - 1
        condition = is_condition_true(little_count)
    print(main_counter)
def is_condition_true(little_count):
    if little_count == 0:
        return True
    else:
        return False
main()

                