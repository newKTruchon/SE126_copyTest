#Lab 2B START with Text File Handling Review

import csv 

total_records = 0

with open("files/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #everything below will occur to EACH record in the file
        #print(rec)

        #rec[0] --> DEVICE TYPES
        device = rec[0]

        if device == "D":

            device = "Desktop"

        elif device == "L":

            device = "Laptop"

        else: #making sure no unexpected values are in the file

            device = "*UNKNOWN*"


        #rec[1] --> BRAND TYPE
        brand = rec[1]

        if brand == "DL":

            brand = "Dell"
        elif brand == "GW":

            brand = "Gateway"
        else:
            brand = brand


        #rec[2] --> PROCESSOR TYPE
        cpu = rec[2]


        #rec[5] --> NUMBER Of HARD DISK DRIVES 
        hdd = int(rec[5])

        if hdd == 1:

            os = rec[6]
            year = rec[7]
            drive2 = "  " #no second drive

        #print the record as requested from the lab prompt
        print("{0}\t\t{1:7}\t\t{2}".format(device, brand, cpu))
        
        total_records += 1

#disconnected from the file 
print("\n\nTOTAL RECORDS: {0}".format(total_records))