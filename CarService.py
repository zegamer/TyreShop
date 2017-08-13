import decimal
import time
import os

modification_date = time.strftime("%m/%d/%y")
file_ext = ".dat"

def calculate_gst():

    print "\n    Calculate CGST + SGST = GST"

    while True:
        try:
            bill = input("\n  Enter Total Bill amount :")
            break
        except:
            print "\nEnter proper value\n"
            
    print "\n  1- 28% GST \n  2- 18% GST \n Default - 28%"

    if raw_input("\n Enter choice(1/2): ") == '2':
        gst = bill * 0.18
    else:
        gst = bill * 0.28

    print "\n Price = {0}\n SGST = {1}\n CGST = {1}\n Total = {2}".format(bill-gst,gst/2.0,bill);

    raw_input("\n\nPress any key to continue...")
    return

def HSN_code():

        print "\n  H S N codes \n"
        print "\n 1: Cars - Radial \n 2: Cars - Nylon \n 3: Buses & Lorries - Radial \n 4: Buses & Lorries - Nylon \n 5: Motor Cycles \n 6: Motor Scooters \n 7: Moped \n 8: Tractor \n 9: TUBE - Cars \n 10: TUBE - Truck/Bus \n 11: TUBE - Motor Cycle \n 12: TUBE - Tractor Front \n 13: TUBE - Tractor Rear \n 14: FLAPS \n 15: JCB etc \n "

        prompt = raw_input("\n> ")

        if prompt == '1':
                print " 4011 10 10"

        elif prompt == '2':
                print " 4011 10 90"

        elif prompt == '3':
                print " 4011 20 10"

        elif prompt == '4':
                print " 4011 20 90"

        elif prompt == '5':
                print " 4011 40 10"

        elif prompt == '6':
                print " 4011 40 20"

        elif prompt == '7':
                print " 4011 40 90"

        elif prompt == '8':
                print " 4011 90 00"

        elif prompt == '9':
                print " 4013 10 10"

        elif prompt == '10':
                print " 4013 10 20"

        elif prompt == '11':
                print " 4013 90 20"

        elif prompt == '12':
                print " 4013 90 49"

        elif prompt == '13':
                print " 4013 90 41"

        elif prompt == '14':
                print " 4012 90 49"

        elif prompt == "15":
                print " 4012 90 20"

        else:
                print "The choice {} could not be found.\n\n".format(prompt)
                time.sleep(1)

        raw_input("\n\nPress any key to continue...")
        return

def add_customer():

        print " ADD CUSTOMER \n\n"
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
               + " Model price \n e.g. NGP 1900.00\n\n"
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
        print "\n 1 = Add new customer "
        print "\n 2 = View existing customer "
        print "\n 3 = Calculate GST "
        print "\n 4 = HSN code "
        print "\n 5 = Exit "

        prompt = raw_input("\n> ")
        os.system("cls")

        if prompt == '1':
                add_tyre()

        elif prompt == '2':
                view_customer()

        elif prompt == '3':
                calculate_gst()

        elif prompt == '4':
                HSN_code()
                
        elif prompt == "5":
                print " EXITING APPLICATION...."
                time.sleep(0.5)
                exit()
        else:
                print "The choice {} could not be found.\n\n".format(prompt)
                time.sleep(1)
                continue
