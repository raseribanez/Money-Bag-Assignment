#!usr/env/bin/python
# Moneybag Weight Checker program
# Written in Python 2.7
# Thinter GUI version - STILL NEEDS TOTALS AT END for coins added and coins removed total values

# Import the required modules
import os
import sys
import Tkinter as tk
from Tkinter import *

# Start the global variable fo total button clicks
presses = 0

# The MAIN pogram - inside a frame
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Variables to handle entrybox data later on
        cvt_from = StringVar()
        cvt_to = StringVar()

        # New click counter Function
        # This will double as the total-bags-checked requirement
        def add_click():
            global presses
            # Add 1 to presses
            presses += 1
            lbl_click_counter.configure(text=presses)

        # Reset Button Function - Closes then re-opens whole application
        # To use this method I had to also import 'os' and 'sys'
        def reset_button_2():
            os.execv(sys.executable, ['python'] + sys.argv)
                        
        # Function 1 to calculate and display the one-pence coin moneybag difference
        def one_pence_bag():
            print"Your moneybag should weigh 356g"
            actual_weight_1 = int(cvt_from.get())
            difference_1 = actual_weight_1 - 356 # If input weight is higher than 356
            difference_2 = 356 - actual_weight_1 # If input weight is lower than 356
            coins_removed_1 = int(difference_1 / 3.56)
            coins_added_1 = int(difference_2 / 3.56)
            if actual_weight_1 > 356:
                cvt_to.set("You need to remove %s One Pence coins" % coins_removed_1)
                print"It is ", int(difference_1), "grams overweight"
                print"============================================"
            if actual_weight_1 < 356:
                cvt_to.set("You need to add %s One Pence coins" % coins_added_1)
                print"It is ", int(difference_2), "grams underweight"
                print"============================================"
            add_click()
           
         # Dont know why uploading added this strange artifact into my code
        # Function 2 to calculate and display the two-pence coin moneybag difference
        def two_pence_bag():
            print("Your moneybag should weigh 356g")
            actual_weight_2 = int(cvt_from.get())
            difference_3 = actual_weight_2 - 356 # If input weight is higher than 356
            difference_4 = 356 - actual_weight_2 # If input weight is lower than 356
            coins_removed_2 = int(difference_3 / 7.12)
            coins_added_2 = int(difference_4 / 7.12)
            if actual_weight_2 > 356:
                cvt_to.set("You need to remove %s Two Pence coins" % coins_removed_2)
                print"It is ", int(difference_3), "grams overweight"
                print"============================================"
            if actual_weight_2 < 356:
                cvt_to.set("You need to add %s Two Pence coins" % coins_added_2)
                print"It is", int(difference_4), 'grams underweight'
                print"============================================"
            add_click()
            
        # Function 3 to calculate and display the five-pence coin moneybag difference
        def five_pence_bag():
            print("Your moneybag should weigh 325g")
            actual_weight_3 = int(cvt_from.get())
            difference_5 = actual_weight_3 - 325 # If input weight is higher than 325difference_6 = 325 - actual_weight_3 # If input weight is lower than 325
            difference_6 = 325 - actual_weight_3   # If input weight is lower then 325
            coins_removed_3 = int(difference_5 / 3.25)
            coins_added_3 = int(difference_6 / 3.25)
            if actual_weight_3 > 325:
                cvt_to.set("You need to remove %s Five Pence coins" % coins_removed_3)
                print"It is ", difference_5, "grams overweight"
                print"============================================"
            if actual_weight_3 < 325:
                cvt_to.set("You need to add %s Five Pence coins " % coins_added_3)
                print"It is ", difference_6, "grams underweight"
                print"============================================"
            add_click()
            
        # Function 4 to calculate and display the ten-pence coin moneybag difference
        def ten_pence_bag():
            print("Your moneybag should weigh 325g")
            actual_weight_4 = int(cvt_from.get())
            difference_7 = actual_weight_4 - 325 # If input weight is higher than 325
            difference_8 = 325 - actual_weight_4 # If input weight is lower than 325
            coins_removed_4 = int(difference_7 / 6.5)
            coins_added_4 = int(difference_8 / 6.5)
            if actual_weight_4 > 325:
                cvt_to.set("You need to remove %s Ten Pence coins" % coins_removed_4)
                print"It is ", difference_7, 'grams overweight'
                print"============================================"
            if actual_weight_4 < 325:
                cvt_to.set("You need to add %s Ten Pence coins" % coins_added_4)
                print"It is ", difference_8, "grams underweight"
                print"============================================"
            add_click()
            
        # Function 5 to calculate and display the twenty-pence coin moneybag difference
        def twenty_pence_bag():
            print"Your moneybag should weigh 250g"
            actual_weight_5 = int(cvt_from.get())
            difference_9 = actual_weight_5 - 250 # If input weight is higher than 250
            difference_10 = 250 - actual_weight_5 # If input weight is lower than 250
            coins_removed_5 = int(difference_9 / 5.0)
            coins_added_5 = int(difference_10 / 5.0)
            if actual_weight_5 > 250:
                cvt_to.set("You need to remove %s Twenty Pence coins" % coins_removed_5 )
                print"It is ", difference_9, "grams overweight"
                print"============================================"
            if actual_weight_5 < 250:
                cvt_to.set("You need to add %s Twenty Pence coins " % coins_added_5)
                print"It is ", difference_10, "grams underweight"
                print"============================================"
            add_click()

        # Function 6 to calculate and display the fifty-pence coin moneybag difference
        def fifty_pence_bag():
            print("Your moneybag should weigh 160g")
            actual_weight_6 = int(cvt_from.get())
            difference_12= actual_weight_6 - 160 # If input weight is higher than 160
            difference_13 = 160 - actual_weight_6 # If input weight is lower than 160
            coins_removed_6 = int(difference_12 / 8.0)
            coins_added_6 = int(difference_13 / 8.0)
            if actual_weight_6 > 160:
                cvt_to.set("You need to remove %s Fifty Pence coins " % coins_removed_6) 
                print"It is", difference_12, "grams overweight"
                print"============================================"
            if actual_weight_6 < 160:
                cvt_to.set("You need to add %s Fifty Pence coins" % coins_added_6)
                print"It is ", difference_13, "grams underweight"
                print"============================================"
            add_click()
       
        # Function 7 to calculate and display the One-pound coin moneybag difference
        def one_pound_bag():
            print("Your moneybag should weigh 190g")
            actual_weight_7 = int(cvt_from.get())
            difference_14 = actual_weight_7 - 190 # If input weight is higher than 190
            difference_15 = 190 - actual_weight_7 # If input weight is lower than 190
            coins_removed_7 = int(difference_14 / 9.50)
            coins_added_7 = int(difference_15 / 9.50)
            if actual_weight_7 > 190:
                cvt_to.set("You need to remove  %s One Pound coins" % coins_removed_7)
                print"It is ", difference_14, "grams overweight"
                print"============================================"
            if actual_weight_7 < 190:
                cvt_to.set("You need to add %s One Pound coins" % coins_added_7)
                print"It is ", difference_15, "grams underweight"
                print"============================================"
            add_click()
        
        # Function 8 to calculate and display the Two-pound coin moneybag difference
        def two_pound_bag():
            print("Your moneybag should weigh 120g")
            actual_weight_8 = int(cvt_from.get())
            difference_16 = actual_weight_8 - 120 # If input weight is higher than 120
            difference_17 = 120 - actual_weight_8 # If input weight is lower than 120
            coins_removed_8 = int(difference_16 / 12)
            coins_added_8 = int(difference_17 / 12)
            if actual_weight_8 > 120:
                cvt_to.set("You need to remove %s Two Pound coins" % coins_removed_8)
                print"It is ", difference_16, "grams overweight"
                print"============================================"
            if actual_weight_8 < 120:
                cvt_to.set("You need to add %s Two pound coins" % coins_added_8)
                print"It is ", difference_17, "grams overweight"
                #print"You've removed %d coins" % coins_added_8
                print"============================================"
            add_click()   

        def count_add_remove():
            totals = [coins_removed_1,
                      coins_added_1,
                      coins_removed_2,
                      coins_added_2,
                      coins_removed_3,
                      coins_added_3,
                      coins_removed_4,
                      coins_added_4,
                      coins_removed_5,
                      coins_added_5,
                      coins_removed_6,
                      coins_added_6,
                      coins_removed_7,
                      coins_added_7,
                      coins_removed_8,
                      coins_added_8]
            print(totals)
            #totals.count = 0
            
        
        # Label to display the user instuctions (enter weight pompt)
        lbl_2 = Label(self, text='Enter the weight of your Money Bag', fg='Blue',font='freesansbold,18')
        lbl_2.pack()

        # Entrybox to gather data
        entry_input = Entry(self, textvariable=cvt_from, font='freesansbold, 18', relief='sunken', justify=CENTER)
        entry_input.pack()

        # Label to display user information (click the right coin type prompt)
        lbl_1 = Label(self, text="Select your Coin Type", font='freesansbold,18', fg='Blue')
        lbl_1.pack()

        # All of the Moneybag value Buttons - with above functions assigned 
        btn_1 = Button(self, text='One Pence Bag', font='12', command=one_pence_bag)
        btn_1.pack(fill=X)
        btn_2 = Button(self, text='Two Pence Bag', font='12', command=two_pence_bag)
        btn_2.pack(fill=X)
        btn_3 = Button(self, text='Five_Pence Bag', font='12', command=five_pence_bag)
        btn_3.pack(fill=X)
        btn_4 = Button(self, text='Ten Pence Bag', font='12', command=ten_pence_bag)
        btn_4.pack(fil=X)
        btn_5 = Button(self, text='Twenty Pence Bag', font='12', command=twenty_pence_bag)
        btn_5.pack(fill=X)
        btn_6 = Button(self, text='Fifty Pence Bag', font='12', command=fifty_pence_bag)
        btn_6.pack(fill=X)
        btn_7 = Button(self, text='One Pound Bag', font='12', command=one_pound_bag)
        btn_7.pack(fill=X)
        btn_8 = Button(self, text='Two Pound Bag', font='12', command=two_pound_bag)
        btn_8.pack(fill=X)

        # Label to Display the results - Beneath the main Buttons
        lbl_result = Label(self, textvariable=cvt_to, font='freesansbold, 16', fg='Blue')
        lbl_result.pack(fill=BOTH, expand=1)

        # Display Click Counter Name
        lbl_click_name = Label(self, text='Total number of bags checked:', font='freesansbold, 14', bg='Grey', fg='Yellow')
        lbl_click_name.pack(fill=X)

        # Display the click-counter
        lbl_click_counter = Label(self, text='', fg='Yellow', font='feesansbold, 18', bg='Grey')
        lbl_click_counter.pack(fill=X)

        # Display total coins added or removed
        #lbl_add_coin = Label(self, text=count_add_remove)#'Label Experiment') #text=coins_added_8)
        #lbl_add_coin.pack()

        # Click for total coins added and removed
        btn_total = Button(self, text='Other Results', command=count_add_remove)
        btn_total.pack()
        
        # Reset Button
        btn_reset = Button(self, text='Reset', fg='Red', font='freesansbold, 14', command=reset_button_2)
        btn_reset.pack(side=BOTTOM, fill=X)

        # Exit Button
        btn_quit = Button(self, text='Exit', fg='Red', font='freesansbold, 14', command=quit)
        btn_quit.pack(side=BOTTOM, fill=X)
        
#  Configure the Main programs window to display MainAplication(frame)
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Money Bag Weight Checker')
    root.minsize(600,700)
    root.configure(bg='Grey')
    MainApplication(root).pack(side="top", fill="both", expand=True)

    # Run the main loop to display EVERYTHING 
    root.mainloop()
