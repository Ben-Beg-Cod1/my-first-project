# dictionaries 

#Roommates_age = {"Synniva" : "26", "Alia": "23", "Leah": "12"}


#print(Roommates_age)


#for roomie in Roommates_age: 
    #print (roomie, Roommates_age[roomie], sep= ",   ")


# dictionaries with multiple key:values e.g. in a table 

Roommates_info = [{"name": "Synniva", "Age": "26", "Height": "1.75m"},
 {"name": "Alia", "Age": "24", "Height": "1.65m"}, 
 {"name": "Leah", "Age": "23", "Height": "1.60m"}, 
 {"name": "Heloise", "Age": "22", "Height": "1.73m"}]

for i in Roommates_info: 
    print (i["name"])
