#WEEK 3 DAY 1: INTRO TO LISTS - DEMO

#LISTS can hold multiple points of data and store them to "memory" to be used later on in our program

#LISTS make it easier to work with file data because they allow us to not have to be connected to to the file/working with the file open in order to process data.

#REMEMBER: when a processor opens and reads a file, it reads ONE record at a time; once a record has been read, the next is read and we      ***CANNOT REACCESS THE RECORD***


#this demo utilizes the lab 2B solution file

import csv

#initialize a var to count the mumber of recs in the file
records = 0 

#PREP EMPTY LISTS -- intiializing a list type with no stored elements to it
#LISTS -- first we need to prep some empty lists so the processor doesn't see one and think it's a var / allows us to store into the list 

#TIP --> create an empty list for EVERY potential field value in the file
device = []
brand = []
cpu = []
ram = []
first_disk = []
no_hdd = []
second_disk = []
os = []
yr = []


with open("images/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 

        #FIELD 0 --> DEVICE TYPES D / L 
        field0 = rec[0] 

        if field0 == "D":

            field0 = "Desktop"

            #rec[0] = "Desktop"

        elif field0 == "L":

            field0 = "Laptop"

        else:

            row = records + 1
            field0 = "*UNKNOWN* @ ROW#" + str(row)

        #FIELD1 --> BRAND  DL, HP, GW
        field1 = rec[1] 

        if field1 == "DL":

            field1 = "Dell"
        
        elif field1 == "GW" :

            field1 = "Gateway"

        else: 

            field1 = field1

        #FIELD 2 --> rec[2] --> PROCESSOR/CPU TYPE
        field2 = rec[2]

        #FIELD 3 --> rec[3] --> RAM
        field3 = rec[3]

        #FIELD 4 --> rec[4] --> FIRST DISK SPACE
        field4 = rec[4]

        #FIELD 5 --> rec[5]  ***DETERMINES EVERYTHING ELSE!***
        field5 = int(rec[5])

        #when num_disks == 1 --> second_disk = none 
        #                    --> os = rec[6]
        #                    --> year = rec[7]


        #when num_disks == 2 --> second_disk = rec[6] 
        #                    --> os = rec[7]
        #                    --> year = rec[8]
        if field5 == 1:

            field6 = "---"
            field7 = rec[6]
            field8 = rec[7]
        
        else:

            field6 = rec[6]
            field7 = rec[7]
            field8 = rec[8]



        #***LIST STORAGE***- you will essentially have a list for every FIELD in your file :]

        #ADD THE FIELD0-8 DATA TO THE APPROPRIATE LISTS
        device.append(field0)
        #<--appending (adding) field0 value into the type list
                            #IF WE HADN'T CREATED VARIABLES for each field:
                            # device.append(rec[0])

        brand.append(field1)
        cpu.append(field2)
        ram.append(field3)
        first_disk.append(field4)
        no_hdd.append(field5)
        second_disk.append(field6)
        os.append(field7)
        yr.append(field8)

        #one print statement for all record displays in file 
        #print("{0:7}\t\t{1:7}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t{6}\t\t{7}\t\t{8}".format(field0, field1, field2, field3, field4, field5, field6, field7, field8))

        records += 1


print("TOTAL RECORDS: {}".format(records))

#the below for loop will start the 'index' value at 0 and run for as many times as the value held inside of 'records'
#the index value will grow by one through each new time through the loop
#INDEX: position inside of the list


#print the text file data from lists
for i in range(0, records):

    #print each record (from the file) by acessing the inidividual lists where its data is stored (each field should have its own list)
    print("INDEX#: {9}\t{0:7}\t\t{1:7}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t{6}\t\t{7}\t\t{8}".format(device[i], brand[i], cpu[i], ram[i], first_disk[i], no_hdd[i], second_disk[i], os[i], yr[i], i))

