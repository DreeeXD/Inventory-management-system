import read
import datetime

#text file update on rent
def update_text(equip_ID, quantity):
    read.dtn[equip_ID][3] = int(read.dtn[equip_ID][3]) - int(quantity)
    dts = read.dtn
    i = 1
    with open("details.txt", "w") as file:
        for values in dts.values():
            if i<5:
                file.write( str(values[0])+ ","+ str(values[1])+ "," + str(values[2])+ "," + str(values[3])+ "\n")
            else:
                file.write( str(values[0])+ ","+ str(values[1])+ "," + str(values[2])+ "," + str(values[3]))
            i += 1
            
"""
This function updates the text file after an item has been rented
It decreases the quantity in the file by quantity purchased by user
"""
            

#generating bill for rented
def ubills(equipDt,uname, umobile, uaddress, r_days, equip_ID, quantity ):
    
    
    date_time = datetime.datetime.now()
    file = open((uname + str(umobile))+".txt", "w")
    file.write("+"+"-"*110+"+ \n")
    file.write("\t\t\t\t\t\t RENT ME" + "\n")
    file.write("\t\t\t\t\t      New York, USA" + "\n")
    file.write("+"+"-"*110+"+ \n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t Date: " + str(datetime.datetime.now().date())+ "\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t Time: "+ str(datetime.datetime.now().time())+ "\n")
    file.write("+"+"-"*110+"+ \n")
    file.write("\t\t\t\t Customer Details" + "\n")
    file.write("Customer Name: "+ uname +"\n")
    file.write("Phone Number: "+ str(umobile) + "\n")
    file.write("Address: "+ uaddress + "\n")
    file.write("+"+"-"*110+"+ \n")
    file.write("\tRented Items"+"\n")
    for i in equipDt:
        file.write(str(i) + "\n")
    file.write("+"+"-"*110+"+ \n")
    file.close()

    return ubills
"""
This function generates the bill 
it also uses for each loop to write the item details from list
"""

#text file update on return
def update_text_return(equip_ID, quantity):
    read.dtn[equip_ID][3] = int(read.dtn[equip_ID][3]) + int(quantity)
    dts = read.dtn
    i = 1
    with open("details.txt", "w") as file:
        for values in dts.values():
            if i<5: #using if else so it doesn't generate a new line each time the text file us updated
                file.write(str(values[0])+ ","+ str(values[1])+ "," + str(values[2])+ "," + str(values[3])+ "\n")
            else:
                file.write(str(values[0])+ ","+ str(values[1])+ "," + str(values[2])+ "," + str(values[3]))
            i += 1
            
#generating bill for return
def return_ubills(equipDt, return_uname, return_umobile, return_uaddress, rented_dayss, returned_date,  return_equip_ID, return_quantity, fine ):
    date_time = datetime.datetime.now()
    file = open((return_uname + str(return_umobile))+".txt", "w")
    file.write("+"+"-"*110+"+ \n" )
    file.write("\t\t\t\t\t\t RENT ME" + "\n")
    file.write("\t\t\t\t\t      New York, USA" + "\n")
    file.write("+"+"-"*110+"+ \n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t Date: " + str(datetime.datetime.now().date())+ "\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t Time: "+ str(datetime.datetime.now().time())+ "\n")
    file.write("+"+"-"*110+"+ \n")
    file.write("\t\t\t\t Customer Details" + "\n")
    file.write("Customer Name: "+ return_uname +"\n")
    file.write("Phone Number: "+ str(return_umobile) + "\n")
    file.write("Address: "+ return_uaddress + "\n")
    file.write("+"+"-"*110+"+ \n")
    file.write("\tRented Items"+"\n")
    for i in equipDt:
        file.write(str(i) + "\n")
    file.write("+"+"-"*110+"+ \n")
    file.close()
