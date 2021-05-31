#Question1a
# i=0
# print ("This program displays the integers from 0 until 25:")
# while(i <= 25):
#     print(i)
#     i=i+1

#Question1b 
# for x in range(26):
#     print (x)

#Question1c
# for x in range(0,26):
#     print (x)

#Question2
# sum=0
# for x in range (10,51):
#     sum = sum+x
#     print ("Adding up:",sum)

#Question3
# userNumber = int(input("Please enter a whole number: "))
# while (userNumber < 50 or userNumber > 70):
#     print ("Not within range.")
#     userNumber = int(input("Please enter a whole number: "))
# print("Within range.")

#Question4
# VariableQ4 = 0
# for VariableQ4 in range (26):
#     print(VariableQ4, end=",")
# print("")

#Question5
# sum=0.0
# VariableQ5 = input("Enter numbers and they will be added together (press x to stop): ")
# while VariableQ5 != "x":
#     sum=sum+int(VariableQ5)
#     print(sum)
#     VariableQ5 = input("Enter numbers and they will be added together (press x to stop): ")
# print(sum)

#Question6
TotalLines = 5
for count in range (TotalLines):
    for count in range (TotalLines):
        print("x", end='')
    print("")

# print ("This program displays a triangle pattern:")
# base_size = 5
# for CountQ in range (base_size):
#     for ThisCanBeAnything in range (CountQ + 1):
#         print (count, end="")
#     print ("")