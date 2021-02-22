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
#functions also need to be defined before we can call them ie use them in our main program code
def celsius_conv(tf):
    #tf is a parameter meaning it is a variable that only exists inside of this function and its value is passed to the function when it is called (see below line in while loop)
    #print("\t\tcelsius_conv()")
    '''this function finds the celsius temp  equivalent'''
    tc = (tf - 32) * (5 / 9)

    return tc
    #by returning tc, we are sending a value back to the point of the function call
#BASE PROGRAM CODE----------------------------------------------------------

#initialize variables - same as "Defining" ie storing an initial value to them
sumtotalTemps = 0
totalTemps = 0

print("\n\n\n\n\n\t\t\tWelcome to my Fahrenheit-to-Celsius Conversion Program")

#answer = input("Enter y to start: ")
tempCount = int(input("\n\t\t\tHow many temps would you like to enter: "))

#while answer == "y":
while tempCount > totalTemps:

    tempF = float(input("\t\t\t\tEnter tempF: "))

    tempC = celsius_conv(tempF)

    #update sumtotal of all tempF values    
    sumtotalTemps += tempF #same as: sumtotalTemps = sumtotalTemps + tempF
    #sumtotalTemps = sumtotalTemps + tempF

    #the way out the of loop!
    totalTemps += 1
    
    print("\t\t\t\tTOTAL TEMPS: ", totalTemps)
    print("\t\t\t\tTemp F is {0:.1f} = Temp C is {1:.1f}".format(tempF, tempC))

    #FOR TESTING --> print("current sum total: ", sumtotalTemps)

    #answer = input("\tWould you like to enter another temperature? [y/n]: ")

#calculate average
avgTempF = sumtotalTemps / totalTemps

avgTempC = celsius_conv(avgTempF)

print("\n\t\t\tTOTAL TEMPERATURES: ", totalTemps)
print("\t\t\tAVERAGE TEMPERATURE: {0:.1f}F | {1:.2f}C".format(avgTempF, avgTempC))

print("\n\n\t\t\tThank you. Goodbye")