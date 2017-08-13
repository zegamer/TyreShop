'''
Had some confusions regarding the user requirements in 
I've made some changes in this program, give it a go.
'''


import decimal
import time
import os

#def main():

# print for current date in mm/dd/yyyy format.
modification_date = time.strftime("%m/%d/%y")
file_ext = ".dat"

def calculate_gst():
    gst=0
    print "\n    Calculate CGST + SGST = GST"
    
    bill = map(double,raw_input("\n  Enter Total Bill amount :"))
    
    print "\n  1- 28% GST \n  2- 18% GST "

    choice = map(int,raw_input("\n Enter choice(1/2): "))
    if choice == 2:
        gst = bill * 0.18
    else:
        gst = bill * 0.28
    
    price = bill - gst
    sgst = gst/2
    print "\n  Price = {0}\n SGST = {1}\n  CGST = {1}\n  Total = {2}".format(price,sgst,bill);
    
    raw_input("\n\nPress any key to continue...")
    return
    

def add_customer():

        print " ADD CUSTOMER \n\n"
# customer info.
        name = raw_input("\nEnter customer's name: ")
        vehicle = raw_input(" Enter the year, make, and model of the vehicle. Example: 2000 Ford Explorer\n> : ")
        cost = decimal.Decimal(raw_input(" How much will the customer be charged? (00.00) rupees : "))
        job = raw_input(" Brief description about services to perform : ")

# append to a list.
        customer_info = {
        "Date:": modification_date,
        "Name:": name,
        "Vehicle:": vehicle,
        "Cost of services:": cost,
        "Description of job:": job
        }

        customer_file = str(customer_info["Name:"]) + file_ext
        customer_file = customer_file.replace(' ', '-')
        customer_file = customer_file.lower()
        print "\n\n"
        with open(customer_file, 'wb') as out_file:
                for field in customer_info:
                        print field, customer_info[field]
                        out_file.write(str(field))
##                        I do not approve of the following line; I simply ran out of coffee.
                        out_file.write(' ' + str(customer_info[field]) + '\n')
                        
        raw_input("\n\nPress any key to continue...")
        return

def add_tyre():
        print " ADD CUSTOMER \n\n"
        
##        Tyre info
        sizeName = raw_input("\n Enter size of tyre : ")
        print ("\n Enter the tyre information in the following format \n"
               + " Model price \n e.g. Wanderer 1900.00\n\n"
               + " Enter 5 values\n")

        tyre_info = {}
        for i in xrange(1,6):
                tyre_info[i] = raw_input("Tyre #" + str(i) + " : ")     
                        
##        Saving to file

        while True:
                inventory = str(sizeName) + file_ext
                inventory = inventory.replace(' ', '-')
                inventory = inventory.lower()
                print "\n\n"

                if file_exists(inventory):
                        inventory = raw_input("File exists !"
                                              + "\n Enter another file name : ")

                else :
                        with open(inventory, 'wb') as out_file:
                                for field in tyre_info:
                                        out_file.write(str(field) + ' ' + str(tyre_info[field]) + '\n')
                        break
                
        raw_input("\n\nPress any key to continue...")
        return
        
def view_customer():
        print " VIEW EXISTING CUSTOMER \n\n"
        name = raw_input("\nEnter customer's name to view records: ")
        customer_file = str(name + file_ext).replace(' ', '-')
        customer_file = customer_file.lower()
        print "\n\n"
        try:
                with open(customer_file, 'rb') as in_file:
                        for line in in_file:
                                print line,
        except IOError:
                print "Error: Cannot find the file for {}".format(name)
                
        raw_input("\n\nPress any key to continue...")
        return

def file_exists(file_name, mode = "r"):
        try:
                f = open(file_name,mode)
                f.close()
                return True
        except IOError:
                return False

## Driver program
while True:
        os.system("cls")
        print " Select a choice: "
        print "\n add = Add new customer "
        print " view = View existing customer "
        print " gst = calculate GST "
        print " exit = Exit "
        
        prompt = raw_input("\n> ").lower()
        os.system("cls")

        if prompt == 'add':
                add_tyre()

        elif prompt == 'view':
                view_customer()
        
        elif prompt == 'gst':
                calculate_gst()

        elif prompt == "exit":
                print " EXITING APPLICATION...."
                time.sleep(0.5)
                exit()
        else:
                print "The choice {} could not be found.\n\n".format(prompt)
                time.sleep(1)
                continue
