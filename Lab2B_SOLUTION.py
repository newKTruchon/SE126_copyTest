#WEEK 3 DAY 1: INTRO TO LISTS - DEMO

#LISTS can hold multiple points of data and store them to "memory" to be used later on in our program

#LISTS make it easier to work with file data because they allow us to not have to be connected to to the file/working with the file open in order to process data.

#REMEMBER: when a processor opens and reads a file, it reads ONE record at a time; once a record has been read, the next is read and we      ***CANNOT REACCESS THE RECORD***


#this demo utilizes the lab 2B solution file

import csv

#initialize a var to count the mumber of recs in the file
records = 0 

print("{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t{5}\t{6}\t{7}\t{8}".format("DEVICE", "BRAND", "CPU", "RAM", "1st DISK", "NUM. DISKS", "2nd DISK", "OS", "YEAR"))
print("-------------------------------------------------------------------------------")

with open("files/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 

        #FIELD 0 --> DEVICE TYPES D / L 
        device = rec[0] 

        if device == "D":

            device = "Desktop"

            #rec[0] = "Desktop"

        elif device == "L":

            device = "Laptop"

        else:

            row = records + 1
            device = "*UNKNOWN* @ ROW#" + str(row)

        #FIELD1 --> BRAND  DL, HP, GW
        brand = rec[1] 

        if brand == "DL":

            brand = "Dell"
        
        elif brand == "GW" :

            brand = "Gateway"

        else: 

            brand = brand

        #FIELD 2 --> rec[2] --> PROCESSOR/CPU TYPE
        cpu = rec[2]

        #FIELD 3 --> rec[3] --> RAM
        ram = rec[3]

        #FIELD 4 --> rec[4] --> FIRST DISK SPACE
        first_disk = rec[4]

        #FIELD 5 --> rec[5]  ***DETERMINES EVERYTHING ELSE!***
        num_disks = int(rec[5])

        #when num_disks == 1 --> second_disk = none 
        #                    --> os = rec[6]
        #                    --> year = rec[7]


        #when num_disks == 2 --> second_disk = rec[6] 
        #                    --> os = rec[7]
        #                    --> year = rec[8]
        if num_disks == 1:

            second_disk = " "
            os = rec[6]
            year = rec[7]
        
        else:

            second_disk = rec[6]
            os = rec[7]
            year = rec[8]



        #one print statement for all record displays in file 
        print("{0:7}\t\t{1:7}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t{6}\t\t{7}\t\t{8}".format(device, brand, cpu, ram, first_disk, num_disks, second_disk, os, year))

        records += 1

print("-------------------------------------------------------------------------------")
print("\nTOTAL RECORDS: {}\n\n".format(records))



