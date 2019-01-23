# import the random module
import random

# create the class Dice
class Dice():

    # create the constructor (__init__) method
    # it takes as input the number sides and if none is specified use 6
    # it sets the dice object's number of sides (instance variable)
    # it sets the list that tracks the rolls to the empty list (instance variable)

    # create the __str__ method
    # if the length of the list that tracks the rolls is 0 it returns "Last roll: not rolled yet"
    # else it returns "Last roll: value" where value is the last value in the list that tracks the rolls

    # create the roll method
    # it randomly picks a value from 1 to the number of sides this dice object has
    # it adds that value to the end of the list that tracks all the rolls
    # it returns the value

    # create the print_history method that prints all the values that have been rolled one per line
    # from the first to the last

    # create the print_count_for_num method
    # it will count how many times the passed number has been rolled and print 
    # number was rolled x times - where number is the number and x is the count
    

# main funtion for testing with a 6 sided and 3 sided die
def main():
    print("Testing a 6 sided die:")
    six_sided = Dice()
    print(six_sided)
    print("Rolled a: " + str(six_sided.roll()))
    print(six_sided)
    for x in range(5):
        print("Rolled a: " + str(six_sided.roll()))
    print("Begin roll history for 6 sided die:")
    six_sided.print_history()
    print("End roll history for 6 sided die.")
    six_sided.print_count_for_num(2)

    #Try out a three sided die
    print("\nTesting a 3 sided die:")
    three_sided = Dice(3)
    print(three_sided)
    print("Rolled a " + str(three_sided.roll()))
    print(three_sided)
    for x in range(5):
        print("Rolled a: " + str(three_sided.roll()))
    print("Begin roll history for 3 sided die:")
    three_sided.print_history()
    print("End roll history for 3 sided die.")
    three_sided.print_count_for_num(2)

# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
