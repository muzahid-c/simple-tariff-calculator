# Simple Tariff Calculator
# Python 2 program
# Author: Munshi Muzahid Hasan Tushar
# Date: 29 August, 2015
# Version: beta 1.0

from tariff import * 
import os, time # For clearing the screen

#-----Main program and interface-----

while True:
    os.system('cls') # clear screen for windows
    os.system('color 0a') # set backgroud color to green and font color to light green 
    print "\n---Simple Tariff Calculator (beta 1.0)---"
    print """\nCustomer type:
1.Residential
2.Commercial
3.Residential Construction
4.Freedom Fighter

99.About\n"""
    print "\nPress q to exit\n"

    category = raw_input("Enter customer type: ")

    os.system('cls')

    if category == '1': # For Residential
        print "\n---Residential---\n"
        print "Press r to return\n"    
        while True:
            kwh_raw = raw_input("Enter(kwh): ")
            if kwh_raw == 'r':
                break
            else:
                kwh = float(kwh_raw)
                print "Money(BDT):", Residential(kwh)
                
        
    elif category == '2': # For Commercial
        print "\n---Commercial---\n"
        print "Press r to return\n"    
        while True:          
            kwh_raw = raw_input("Enter(kwh): ")
            if kwh_raw == 'r':
                break
            else:
                kwh = float(kwh_raw)
                print "Money(BDT):", Commercial(kwh)
            
    elif category == '3': # For Residential Construction
        print "\n---Residential Construction---\n"
        print "Press r to return\n"
        while True:
            kwh_raw = raw_input("Enter(kwh): ")
            if kwh_raw == 'r':
                break
            else:
                kwh = float(kwh_raw)
                print "Money(BDT):", ResidentialConstruction(kwh)
            
    elif category == '4': # For Freedom Fighter
        print "\n---Residential Freedom Fighter---\n"
        print "Press r to return\n"    
        while True:
            kwh_raw = raw_input("Enter(kwh): ")
            if kwh_raw == 'r':
                break
            else:
                kwh = float(kwh_raw)
                print "Money(BDT):", ResidentialFF(kwh)

    elif category == '99':
            while True:
                    os.system('cls')
                    print """

        Simple Tariff Calculator
        Version: beta 1.0
        Date: 29 August, 2015
        Author: Munshi Muzahid Hasan Tushar

        """
                    print "Press r to return"
                    press = raw_input()
                    if press == 'r':
                            break # Return to main function
                                
    elif category == 'q':
        print "\nbye"
        time.sleep(1)
        break

    elif category == 'open':
            while True:
                    os.system('cls')
                    print """

        You will never find a software that will meet all your demand.
        So write one!
        """
                    press = raw_input()
                    if press == 'r':
                            break # Return to main function
        

    else:
        print "\nInvalid choice!\n"
        time.sleep(2)
        continue
    
