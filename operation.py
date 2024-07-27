import read
import write

rented_items = []
totals =  []
return_totals = []
return_items = []

def valid_equipmentID():
#getting ID for equipment rental
    try:
        equip_ID = int(input("Please enter the equipment Id for equipment you would like to rent: "))
        
#checking ID if correct or not and trying again
        while equip_ID <= 0 or equip_ID > len(read.dtn):
            print("Please Use Correct Equipment ID and Try Again!")
            equip_ID = int(input("Please enter the equipment Id for equipment you would like to rent: "))
        print(read.dtn[equip_ID])
    except ValueError:
    #if input is invalid then it will ask user to try again until they give a correct value of id
        print("Error! Invalid Input!")
        return valid_equipmentID()
    return equip_ID


def equipment_valid_quantity(equip_ID):
 #getting quantity for equipment rental
    try:
        valid_quantity = read.dtn[equip_ID][3]
        if int(valid_quantity) <= 0:
            print("Sorry, the selected equipment is not available. Please Select a different one.")
            return 0
        
        quantity = int(input("Please enter the quantity for your rental: "))

        #checking if quantity is valid or not
        valid_quantity = read.dtn[equip_ID][3]
        while quantity <=0 or quantity > int(valid_quantity):
            print("Please check the available quantity and try again.")

            quantity = int(input("Please enter the quantity for your rental: "))

    except ValueError:
    #if input is invalid then it will ask user to try again until they give a correct value of quantity
        print("Invalid Quantity")
        return equipment_valid_quantity(equip_ID)
    return quantity


def rent_days():
#getting the rental days
    try:
        r_days = int(input("Enter the number of days you want to rent the equipment: "))
        #checking if days are valid or not
        while r_days<= 0:
            print("Please enter valid rental days!")
            r_days = int(input("Enter the number of days you want to rent the equipment: "))
    
    except ValueError:
        print("Invalid Input!")
    
        return rent_days()
    return r_days

def per_day_crg(r_days):
    if r_days % 5 == 0:
        crg = r_days // 5
    else:
        crg = r_days // 5+1
    return crg


def user_purchased(equip_ID, quantity, crg):
#getting items purchased by user
    userProduct= read.dtn[equip_ID][0]
    userQuantity = quantity
    itemPrice = read.dtn[equip_ID][2].replace("$", "")
    totalprice = int(userQuantity) * int(itemPrice) * crg

    #rented_items.append((userProduct, int(itemPrice), userQuantity, crg))
    return totalprice

def user_pur(userProduct, quantity, uprice, totalprice):
    #appending user rented items into a list
    user_p_items = []
    user_p_items.append((userProduct, quantity, uprice, totalprice))
    return user_p_items

def billAll():
    rented_items.append("Grand Total: "+ str(sum(totals)))
    return rented_items

def rent_more(equip_ID, r_days, quantity, crg):
    #to be called if user wants to rent more than one item
    total_price = 0
    global rented_items
    crg = per_day_crg(r_days)
    total_price += user_purchased(equip_ID, quantity, crg)
    #rented_items.append((read.dtn[equip_ID][0], quantity,  read.dtn[equip_ID][2], total_price))
    totals.append(int(total_price)) 
    rented_items.append("Equipment Name: "+ str(read.dtn[equip_ID][0])+"\n")
    rented_items.append("Rented Days: "+ str(quantity) + "\n")
    rented_items.append("Equipment Brand: "+ str(read.dtn[equip_ID][1]) + "\n")
    rented_items.append("Item Price: "+str(read.dtn[equip_ID][2]) + "\n")
    rented_items.append("Equipment Quantity: "+ str(r_days) + "\n")

    return rented_items
                
                
def udetails():
    #asking details of user for printing invoice
    print("For Generating Invoice, Please Fill up the Required Data!")
    try:
        uname = input("Enter your Name: ")
        umobile = int(input("Enter your Phone number: "))
        if umobile<0:
            print("Please Provide us valid number")
            return udetails()
        uaddress = input("Enter your Address: ")
    except ValueError:
        print("Please provide valid input.")
        return udetails()
    return uname, umobile, uaddress

"""
Defining all the functions here 
so it'd be easier to access them in main.py
"""


#---------------------------------------Defining Return Functions-----------------------------------------------#



def return_equip_id():
    #getting ID for equipment return
    try:
        return_equip_ID = int(input("Please enter the equipment Id for equipment you would like to return: "))
        
#checking ID if correct or not and trying again
        while return_equip_ID <= 0 or return_equip_ID > len(read.dtn):
            print("Please Use Correct Equipment ID and Try Again!")
            return_equip_ID = int(input("Please enter the equipment Id for equipment you would like to return: "))
        print(read.dtn[return_equip_ID])
    except ValueError:
    #if input is invalid then it will ask user to try again until they give a correct value of id
        print("Error! Invalid Input!")
        return return_equip_id()
    return return_equip_ID


def return_equipment_valid_quantity(return_equip_ID):
 #getting quantity for equipment return
    try:
        return_quantity = int(input("Please enter the quantity for your return: "))

        #checking if quantity is valid or not
        return_valid_quantity = read.dtn[return_equip_ID][3]
        while return_quantity <=0:
            print("Please check the quantity and try again.")

            return_quantity = int(input("Please enter the quantity for your return: "))

    except ValueError:
    #if input is invalid then it will ask user to try again until they give a correct value of quantity
        print("Invalid Quantity")
        return return_equipment_valid_quantity()
    return return_quantity

def rented_days():
#getting the rental days
    try:
        rented_dayss = int(input("Enter the number of days you rented the equipment: "))
        #checking if rented days are valid or not
        while rented_dayss <= 0:
            print("Please enter valid rented days!")
            rented_dayss = int(input("Enter the number of days you rented the equipment: "))
    
    except ValueError:
        print("Invalid Input!")
    
        return rented_days()
    return rented_dayss


def return_days():
    #getting when the customer returned the equipment
    try:
        return_date = int(input("Enter the days you rented the item for: "))
        #checking if days are valid or not
        while return_date <= 0:
            print("Please enter valid days!")
            return_date = int(input("Enter the days you rented the item for: "))

    except ValueError:
        print("Invalid Input!")
        return return_days()
    return return_date


#getting the fine, if user is late returning the item
# def per_daycrg_returndays(return_date):
#     if return_date % 5 == 0:
#         return_crg = return_date // 5
#     else:
#         return_crg = (return_date // 5)+1
#     return return_crg

# def per_daycrg_renteddays(rented_dayss):
#     if rented_dayss % 5 == 0:
#         rentedd_crg = rented_dayss // 5
#     else:
#         rentedd_crg = (rented_dayss // 5)+1
#     return rentedd_crg



# def fine(return_equip_ID, return_quantity, rented_dayss, return_date):
#     item_value = int(read.dtn[return_equip_ID][2].strip().replace("$", ""))
    
#     if rented_dayss < return_date:
#         fine_days = return_date - rented_dayss
#         returned_fine = per_daycrg_returndays(return_date) * item_value *  fine_days
#         rented_fine = per_daycrg_renteddays(rented_dayss) * item_value * fine_days
        
#         fine = (returned_fine - rented_fine) * return_quantity
#         return int(fine), fine_days, rented_dayss, rented_fine
    
#     else: 
#         rented_fine = per_daycrg_renteddays(rented_dayss) * item_value * rented_dayss
#         return 0

def calculate_fine(rented_days, return_date, quantity, item_price):
    if rented_days < return_date:
        extra_days = return_date - rented_days
        charge_per_period = 5  # Charge is applied on a 5-day basis
        fine_periods = extra_days // charge_per_period
        fine = fine_periods * int(item_price) * quantity
        return fine
    else:
        return 0


def user_rented(return_equip_ID, return_quantity, fine):
    return_userProduct = read.dtn[return_equip_ID][0]
    returned_userQuantity = return_quantity
    returned_itemPrice = str(read.dtn[return_equip_ID][2]).replace("$", "")
    returned_totalprice = int(returned_userQuantity) * int(returned_itemPrice) * fine
    return returned_totalprice

def user_return(returned_userProduct, quantity, returned_uprice, returned_totalprice):
    #appending user returned items in a list
    user_return_items = []
    user_return_items.append((returned_userProduct, quantity, returned_uprice, returned_totalprice))
    return user_return_items

def return_billAll():
    return return_items

# def return_more(return_equip_ID, rented_dayss, return_date, return_quantity, fined):
# #if user wants to return more than one item
#     returned_total_price = 0
#     global return_items
#     returned_total_price = user_rented(return_equip_ID, return_quantity, fined)[3]
#     fines = fine(return_equip_ID, return_quantity, rented_dayss, return_date)

#     #rented_items.append((read.dtn[equip_ID][0], quantity,  read.dtn[equip_ID][2], total_price))
#     return_items.append("Equipment Name: "+ str(read.dtn[return_equip_ID][0])+"\n")
#     return_items.append("Rent Days: "+ str(rented_dayss) + "\n")
#     return_items.append("Rented Days: "+ str(return_date) + "\n")
#     return_items.append("Equipment Brand: "+ str(read.dtn[return_equip_ID][1]) + "\n")
#     return_items.append("Item Price: "+str(read.dtn[return_equip_ID][2]) + "\n")
#     return_items.append("Equipment Quantity: "+ str(return_quantity) + "\n")

#     return_totals.append(int(returned_total_price))
#     grand_total = sum(return_totals)
#     return_items.append("Grand Total: "+ str(grand_total))
#     return return_items

def return_more(return_equip_ID, rented_dayss, return_date, return_quantity, fined):
    
    return_totals.clear() #such that the list is empty before appending
    returned_total_price = user_rented(return_equip_ID, return_quantity, fined)

    fines = calculate_fine(return_equip_ID, return_quantity, rented_dayss, return_date)

    return_totals.append(returned_total_price)

    grand_total = sum(return_totals)

    # Update the return_items list with the equipment details
    return_items.append("Equipment Name: " + str(read.dtn[return_equip_ID][0]) + "\n")
    return_items.append("Rent Days: " + str(rented_dayss) + "\n")
    return_items.append("Returned Days: " + str(return_date) + "\n")
    return_items.append("Equipment Brand: " + str(read.dtn[return_equip_ID][1]) + "\n")
    return_items.append("Item Price: " + str(read.dtn[return_equip_ID][2]) + "\n")
    return_items.append("Equipment Quantity: " + str(return_quantity) + "\n")

    # Append the grand total to the return_items list
    return_items.append("Grand Total: " + str(grand_total))

    return return_items
            
def return_udetails():
#asking user details such to genearte an invoice
    print("For Generating Invoice, Please Fill up the Required Data!")
    try:
        return_uname = input("Enter your Name: ")
        return_umobile = int(input("Enter your Phone number: "))
        if return_umobile< 0:
            print("Please Enter Valid Input")
            return return_udetails()
        return_uaddress = input("Enter your Address: ")
    except ValueError:
        print("Please provide valid input.")
        return return_udetails()
    return return_uname, return_umobile, return_uaddress
