#Explaining the program
print("\nHello world. Today we are adding two numbers together.\n")
#Asking for two numbers
num1 = (input("Type your first number here: "))
num2 = (input("Type your second number here: "))
#creating the total by adding two numbers together
total = int(num1) + int(num2)
print("\nThank you. We're adding the two numbers together...\n")
#Opening the file.
Maths_file = open ('Maths.txt', 'w')
#Adding two numbers together 
print(num1,"+",num2,"=",total)
print(num1," + ",num2," = ",total,file=Maths_file)
Maths_file.close
#Letting user know we have outputted the final equation into a file called 'maths.txt'.
print("\nThe result has been printed into a file called Maths.txt for your future reference. Thanks again.\n")