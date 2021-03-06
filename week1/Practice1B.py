#Practice 1B SOLUTION FILE

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#* comments are lines that were suggested to change from Practice 1A in order to complete Practice 1B

#VARIABLE DICTIONARY---------
#sumtotalTemps          the sum total of all F temps entered during session
#totalGTemps            the number of temps entered during session

#FUNCTIONS------------------------------------------------------------------

#BASE PROGRAM CODE----------------------------------------------------------

#initialize variables
sumtotalTemps = 0
totalTemps = 0


print("Welcome to my Fahrenheit-to-Celsius Conversion Program")

#*answer = input("Enter y to start: ")*
tempCount = int(input("\nHow many temperatures would you like to check: "))

#*while answer == "y" or answer == "Y":*
while tempCount > totalTemps:

    tempF = float(input("\tEnter tempF: "))

    tempC = (tempF - 32) * (5 / 9)

    #update sumtotal of all tempF values    
    sumtotalTemps += tempF #same as: sumtotalTemps = sumtotalTemps + tempF

    #the way out of the loop now!
    totalTemps += 1
    
    print("\tTOTAL TEMPS: ", totalTemps)
    print("\tTemp F is {0:.1f} = Temp C is {1:.1f}".format(tempF, tempC))

    #FOR TESTING --> print("current sum total: ", sumtotalTemps)

    #*answer = input("\tWould you like to enter another temperature? [y/n]: ")*

#calculate average
avgTempF = sumtotalTemps / totalTemps

avgTempC = (avgTempF - 32) * (5 / 9)

print("\nTOTAL TEMPERATURES: ", totalTemps)
print("AVERAGE TEMPERATURE: {0:.1f}F | {1:.2f}C".format(avgTempF, avgTempC))

print("\n\nThank you. Goodbye")