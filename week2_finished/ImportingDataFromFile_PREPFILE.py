#Week 2 Day 2: Importing Data from a File

#YOU MUST IMPORT THE CSV LIBRARY IN ORDER FOR FILES TO BE ACCESSED

#CSV: Comma Separated Values
#RECORDS: rows of the file, different types of data all belonging together
#FIELDS: columns of the file, sets of data (all data in a column is the same "type" ie names, ages, salaries, email addresses, etc)

#BASE PROGRAM CODE-------------------------------------------------------------------

#STEP 1: import csv library so we can read the file
import csv

#you should ALWAYS have a total records var for your first few attempts at file reading
total_records = 0

#holds all salaries in file for total print at end
total_salaries = 0

#prnt header -- at the end, once everything else is running accurately
print("{0} \t {1} \t {2}".format("NAME", "AGE", "SALARY"))
print("-----------------------------------------------")

#STEP 2: CONNNECT TO THE FILE LOCATION
#right-click the text/csv file in folder view --> "Properties" to find the file location
#these file locations are cAsE sEnSiTiVe & space/special character sensitive so DOUBLE CHECK THEM!
#flip all '\' to '/'
with open("week2/example.csv") as csvfile:
    
    #notice ':' everything must be INDENTED now (until we're ready to "close" the file)

    #STEP 3: ALLOW THE FILE TO BE READ BY OUR PROGRAM
    file = csv.reader(csvfile)

    
    #STEP 4: ACTUALLY READ/PROCESS THE FILE DATA, ONE RECORD AT A TIME
    for rec in file:

        total_records += 1

        name = rec[0] 
        age = int(rec[1])
        money = float(rec[2])

        print("{0:8} \t {1:3} \t {2:7.2f}".format(name, age, money)) 

        #add all salaries to total_salary -- REMEMBER: all data entering a Python program is treated as a STRING unless cast otherwise
        total_salaries += money


        
        
        #add field width to ensure columns stay aligned
print("\n\n\nPROGRAM DONE.")
 
print("\n\n")
#print final values: total records processed and total salary of all employees in file
print("TOTAL RECORDS: ", total_records)
print("TOTAL SALARY: ${0:,.2f}".format(total_salaries))