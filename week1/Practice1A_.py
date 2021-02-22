#Practice 1A SOLUTION FILE

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------
#sumtotalTemps          the sum total of all F temps entered during session
#totalGTemps            the number of temps entered during session

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

#initialize variables - same as "Defining" ie storing an initial value to them
sumtotalTemps = 0
totalTemps = 0

print("\n\n\n\n\n\t\t\tWelcome to my Fahrenheit-to-Celsius Conversion Program")

answer = input("Enter y to start: ")


while answer == "y":


    tempF = float(input("\t\t\t\tEnter tempF: "))

    tempC = celsius_conv(tempF)

    #update sumtotal of all tempF values    
    sumtotalTemps += tempF #same as: sumtotalTemps = sumtotalTemps + tempF
    #sumtotalTemps = sumtotalTemps + tempF

    
    totalTemps += 1
    
    print("\t\t\t\tTOTAL TEMPS: ", totalTemps)
    print("\t\t\t\tTemp F is {0:.1f} = Temp C is {1:.1f}".format(tempF, tempC))

    #FOR TESTING --> print("current sum total: ", sumtotalTemps)

    answer = input("\tWould you like to enter another temperature? [y/n]: ")

#calculate average
avgTempF = sumtotalTemps / totalTemps

avgTempC = celsius_conv(avgTempF)

print("\n\t\t\tTOTAL TEMPERATURES: ", totalTemps)
print("\t\t\tAVERAGE TEMPERATURE: {0:.1f}F | {1:.2f}C".format(avgTempF, avgTempC))

print("\n\n\t\t\tThank you. Goodbye")