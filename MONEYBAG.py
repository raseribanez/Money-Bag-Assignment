# Money Bag weight checker program
# Written and runs in Python 2.7
#!usr/bin/env/python

# while loops
# if statements
# else statements
# functions
# conversions (float to int)


def main():
  
    def one_pence_coin():
        print("Your moneybag should weigh 356g")
          
        difference_1 = bag_weight - 356 # If input weight is higher than 356
        difference_2 = 356 - bag_weight # If input weight is lower than 356
        coins_removed_1 = int(difference_1 / 3.56)
        coins_added_1 = int(difference_2 / 3.56)
        if bag_weight > 356:
            print("You need to remove %s One Pence coins" % coins_removed_1)
            print"It is ", int(difference_1), "grams overweight"
            print("============================================")
        if bag_weight < 356:
            print("You need to add %s One Pence coins" % coins_added_1)
            print"It is ", int(difference_2), "grams underweight"
            print("============================================")

    # Function 2 to handle the 2 pence coins
    def two_pence_coin():
        print("Your moneybag should weigh 356g")
        difference_3 = bag_weight - 356 # If input weight is higher than 356
        difference_4 = 356 - bag_weight # If input weight is lower than 356
        coins_removed_2 = int(difference_3 / 7.12)
        coins_added_2 = int(difference_4 / 7.12)
        if bag_weight > 356:
            print("You need to remove %s Two Pence coins" % coins_removed_2)
            print"It is ", int(difference_3), "grams overweight"
            print"============================================"
        if bag_weight < 356:
            print("You need to add %s Two Pence coins" % coins_added_2)
            print"It is", int(difference_4), 'grams underweight'
            print"============================================"
        
    # Function 3 to handle the 5 pence coin
    def five_pence_coin():
        print("Your moneybag should weigh 325g")
        difference_5 = bag_weight - 325 # If input weight is higher than 325difference_6 = 325 - actual_weight_3 # If input weight is lower than 325
        difference_6 = 325 - bag_weight   # If input weight is lower then 325
        coins_removed_3 = int(difference_5 / 3.25)
        coins_added_3 = int(difference_6 / 3.25)
        if bag_weight > 325:
            print("You need to remove %s Five Pence coins" % coins_removed_3)
            print"It is ", difference_5, "grams overweight"
            print"============================================"
        if bag_weight < 325:
            print("You need to add %s Five Pence coins " % coins_added_3)
            print"It is ", difference_6, "grams underweight"
            print"============================================"

    # Function 4 to handle the 10 pence coins
    def ten_pence_coin():
        print("Your moneybag should weigh 325g")
        difference_7 = bag_weight - 325 # If input weight is higher than 325
        difference_8 = 325 - bag_weight # If input weight is lower than 325
        coins_removed_4 = int(difference_7 / 6.5)
        coins_added_4 = int(difference_8 / 6.5)
        if bag_weight > 325:
            print("You need to remove %s Ten Pence coins" % coins_removed_4)
            print"It is ", difference_7, 'grams overweight'
            print"============================================"
        if bag_weight < 325:
            print("You need to add %s Ten Pence coins" % coins_added_4)
            print"It is ", difference_8, "grams underweight"
            print"============================================"
        
    # Function 5 to handle the 20 pence coins
    def twenty_pence_coin():
        print"Your moneybag should weigh 250g"
        difference_9 = bag_weight - 250 # If input weight is higher than 250
        difference_10 = 250 - bag_weight # If input weight is lower than 250
        coins_removed_5 = int(difference_9 / 5.0)
        coins_added_5 = int(difference_10 / 5.0)
        if bag_weight > 250:
            print("You need to remove %s Twenty Pence coins" % coins_removed_5 )
            print"It is ", difference_9, "grams overweight"
            print"============================================"
        if bag_weight < 250:
            print("You need to add %s Twenty Pence coins " % coins_added_5)
            print"It is ", difference_10, "grams underweight"
            print"============================================"

    # Function 6 to calculate and display the fifty-pence coins
    def fifty_pence_coin():
        print("Your moneybag should weigh 160g")
        difference_12= bag_weight - 160 # If input weight is higher than 160
        difference_13 = 160 - bag_weight # If input weight is lower than 160
        coins_removed_6 = int(difference_12 / 8.0)
        coins_added_6 = int(difference_13 / 8.0)
        if bag_weight > 160:
            print("You need to remove %s Fifty Pence coins " % coins_removed_6) 
            print"It is", difference_12, "grams overweight"
            print"============================================"
        if bag_weight < 160:
            print("You need to add %s Fifty Pence coins" % coins_added_6)
            print"It is ", difference_13, "grams underweight"
            print"============================================"

    # Function 7 to calculate and display the One-pound coin
    def one_pound_coin():
        print("Your moneybag should weigh 190g")
        difference_14 = bag_weight - 190 # If input weight is higher than 190
        difference_15 = 190 - bag_weight # If input weight is lower than 190
        coins_removed_7 = int(difference_14 / 9.50)
        coins_added_7 = int(difference_15 / 9.50)
        if bag_weight > 190:
            print("You need to remove  %s One Pound coins" % coins_removed_7)
            print"It is ", difference_14, "grams overweight"
            print"============================================"
        if bag_weight < 190:
            print("You need to add %s One Pound coins" % coins_added_7)
            print"It is ", difference_15, "grams underweight"
            print"============================================"

    # Function 8 to calculate and display the Two-pound coin
    def two_pound_coin():
        print("Your moneybag should weigh 120g")
        difference_16 = bag_weight - 120 # If input weight is higher than 120
        difference_17 = 120 - bag_weight # If input weight is lower than 120
        coins_removed_8 = int(difference_16 / 12)
        coins_added_8 = int(difference_17 / 12)
        if bag_weight > 120:
            print("You need to remove %s Two Pound coins" % coins_removed_8)
            print"It is ", difference_16, "grams overweight"
            print"============================================"
        if bag_weight < 120:
            print("You need to add %s Two pound coins" % coins_added_8)
            print"It is ", difference_17, "grams overweight"
            print"============================================"

    # Function to handle the different bag_types
    def handle_bags():
            if bag_type == 1:
                one_pence_coin()
            if bag_type == 2:
                two_pence_coin()
            if bag_type == 3:
                five_pence_coin()
            if bag_type == 4:
                ten_pence_coin()
            if bag_type == 5:
                twenty_pence_coin()
            if bag_type == 6:
                fifty_pence_coin()
            if bag_type == 7:
                one_pound_coin()
            if bag_type == 8:
                two_pound_coin()

    # Function to handle resetting the program
    def restart_program():
        while True:
            restart = input("Do you want to check another MoneyBag? Enter '1' for YES and '2' for NO\n>>>")
            if restart ==1:
                main()
            else:
                print "Thanks for using the Weight Checker"
                break


    # Call the functions in the right order
    bag_weight = int(input("Enter the weight of your bag\n>>>"))
    bag_type = int(input("Enter one of the following coin type Numbers: \nOnePence: 1 \nTwoPence: 2 \nFivePence: 3 \nTenPence: 4 \nTwentyPence: 5 \nFiftyPence: 6 \nOnePound: 7 \nTwoPound: 8 \n>>>"))
    handle_bags()
    restart_program()

# Main program function
main()
    


