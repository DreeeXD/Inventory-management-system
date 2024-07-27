file = open("details.txt", "r")
equip = file.read()
file.close()
split_equip = equip.split("\n")
no = 1
dtn = {} 
for i in range(len(split_equip)):
    dtn[no] = split_equip[i].split(",")
    no += 1
    
"""
This reads the text file 
and puts them in a dictionary which makes it easier 
to access them throughout the program
"""