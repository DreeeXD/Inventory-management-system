#importing necessary modules
import read
import write
import operation

"""
This function below opens the file and using for loop, displays
it in a tabular form.
"""

def display_file():
    print("-" * 110)
    print("||Equipment No \t     Equipment Name \t\t Brand  \t\t  Price   \t      Quantity ||")
    print("-" * 110)
    equipmentsss = open("details.txt", "r")
    equipmentNo = 1
    for i in equipmentsss:
        print("    ", equipmentNo, "\t\t\t", i.replace(",", "\t\t\t "))
        equipmentNo += 1
    print("-" * 110)
    print("\n")
    equipmentsss.close()


def startup():
    name = input("Enter Your Name: ")
    print("\nWelcome,",name+"!!" + " Please Select an Option Below :)\n")

    option = True
    while option == True:
        print("Type 1 to Display Available Equipments")
        print("Type 2 for Equipment Rental")
        print("Type 3 for Equipment Return")
        print("Type 4 to Exit")
        ans = input("Enter Your Choice Here: ")
        if ans == "1":
            display_file()
            print(name+"!!" " What would you like to do? \n")
            option = True
            
        elif ans == "2":
            print("\nStarting Rental Procedures\n")
            option = True
            display_file()

            #calling all the functions required for the rental procedure from operation.py
            rent_equipID = operation.valid_equipmentID()
            available_quantity = read.dtn[rent_equipID][3]
            print("Availale Quantity: ", available_quantity)
            if int(available_quantity) > 0:
                rent_quantity = operation.equipment_valid_quantity(rent_equipID)
                
                if rent_quantity > int(available_quantity):
                    print("The selected item is not available.")
                else:
                    days_rent = operation.rent_days()
                    chargee = operation.per_day_crg(days_rent)
                    rent_text_update = write.update_text(rent_equipID, rent_quantity)
                    total_price = operation.user_purchased(rent_equipID, rent_quantity, chargee)
                    operation.rented_items.append((read.dtn[rent_equipID][0], int(read.dtn[rent_equipID][2].replace("$", " ")), rent_quantity, chargee))
                    rent_again = operation.rent_more(rent_equipID, rent_quantity, days_rent, chargee)
                    #using while loop such that if customer wants to rent again, they can rent until their choice is "n"
                    while True:
                        print()
                        print("Do you want to rent again")
                        choice = input("Enter y or n: ")
                        if choice == "y":
                            display_file()
                            rent_equipID = operation.valid_equipmentID()
                            available_quantity = read.dtn[rent_equipID][3]
                            print("availale: ", available_quantity)
                            if int(available_quantity) > 0:
                                rent_quantity = operation.equipment_valid_quantity(rent_equipID)
                
                                if rent_quantity > int(available_quantity):
                                    print("The selected item is not available.")
                                else:
                                    days_rent = operation.rent_days()
                                    chargee = operation.per_day_crg(days_rent)
                                    rent_text_update = write.update_text(rent_equipID, rent_quantity)
                                    total_price = operation.user_purchased(rent_equipID, rent_quantity, chargee)
                                    operation.rented_items.append((read.dtn[rent_equipID][0], int(read.dtn[rent_equipID][2].replace("$", " ")), rent_quantity, chargee))
                                    rent_again = operation.rent_more(rent_equipID, rent_quantity, days_rent, chargee)
                        elif choice == "n":
                            break
                        else:
                            print("Invalid Input, Please try again")

                    user_name, user_number, user_address = operation.udetails()
                    equipDtl = operation.billAll()
                    generatebill = write.ubills(equipDtl,user_name, user_number, user_address, days_rent, rent_equipID, rent_quantity)
            else:
                print("Sorry, We are out of stock for the selected item.")
            option = True
            

        
        elif ans == "3":
            print("\nStarting Return Procedures\n")
            option = True
            display_file()
            
            #calling the functions required for the return procedure from operation.py
            return_equipID = operation.return_equip_id()
            return_quantity = operation.return_equipment_valid_quantity(return_equipID)
            days_rented = operation.rented_days()
            days_returned = operation.return_days()
            item_pricee = read.dtn[return_equipID][2].replace("$", "")
            fine = operation.calculate_fine(days_rented, days_returned, return_quantity, item_pricee)
            #per_day_charge_return = operation.per_daycrg_returndays(days_returned)
            #per_day_charge_rent = operation.per_daycrg_renteddays(days_rented)
            return_text_update = write.update_text_return(return_equipID, return_quantity)
            returned_total_price = operation.user_rented(return_equipID, return_quantity, fine)
            operation.return_items.append((read.dtn[return_equipID][0], int(read.dtn[return_equipID][2].replace("$", " ")), return_quantity, fine))
            return_again = operation.return_more(return_equipID, days_rented, days_returned, return_quantity, fine)

            while True:
                print()
                print("Do you want to return again?")
                choice = input("Enter y or n: ")
                if choice == "y":
                    display_file()
                    return_equipID = operation.return_equip_id()
                    return_quantity = operation.return_equipment_valid_quantity(return_equipID)
                    days_rented = operation.rented_days()
                    days_returned = operation.return_days()
                    item_pricee = read.dtn[return_equipID][2].replace("$", "")
                    #per_day_charge_return = operation.per_daycrg_returndays(days_returned)
                    #per_day_charge_rent = operation.per_daycrg_renteddays(days_rented)
                    return_text_update = write.update_text_return(return_equipID, return_quantity)
                    fine = operation.calculate_fine(days_rented, days_returned, return_quantity, item_pricee)
                    returned_total_price = operation.user_rented(return_equipID, return_quantity, fine)
                    operation.return_items.append((read.dtn[return_equipID][0], int(read.dtn[return_equipID][2].replace("$", " ")), return_quantity, fine))
                    return_again = operation.return_more(return_equipID, days_rented, days_returned, return_quantity, fine)

                elif choice == "n":
                    break
                else:
                    print("Invalid Input, Please try again")

            return_user_name, return_user_number, return_user_address = operation.return_udetails()
            equipDt2 = operation.return_billAll()
            generatebill = write.return_ubills(equipDt2 , return_user_name, return_user_number, return_user_address, days_rented, days_returned, return_equipID, return_quantity, fine)

        elif ans == "4":
            print("\nExiting the command")
            option = False

        else:
            print("\nINVALID INPUT... PLEASE TRY AGAIN!!!")
            option = True
            
startup()
