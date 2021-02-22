#FUNCTIONS are reusable pieces of code; they are written once in the file and can be called (used) as many times as necessary

#A function must be defined before you can use it
def functionName(n1, n2):
    '''This is an addition function''' 

    answer = n1 + n2 

    return answer

print(answer)   

#gather necessary data
num1 = int(input("      Enter a number: "))
num2 = int(input("Enter another number:"))


#call the function in order to use it! 
#pass values so the function can do its job 
sumAnswer = functionName(num1, num2)

print("The SUM of {0} + {1} = {2:.1f}".format(num1, num2, sumAnswer))
