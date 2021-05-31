# states = ["VIC","NSW","SA","WA","TAS","QLD","ACT"]
# print(states)
# states.remove("ACT")
# print(states)

# words = "Hello world I am here"
# print (words)
# print (words.split("w"))

# numbers = list(range(10))
# print(len(numbers))
# print(numbers)
# print(numbers[1+numbers[5]])

#QUIZ BEGINS

#Q1
# values = [66, 43, 1, 6, 2, 99, 4]
# i = 0
# while (i < len(values)):
#     if(values[i] < 10):
#         print(values[i])
#     i += 1

#Q2
# userDate = input("Please enter the date in the format DD/MM/YYYY: ")
# userDateSeparated = userDate.split("/")
# print("Day:",userDateSeparated[0])
# print("Month:",userDateSeparated[1])
# print("Year:",userDateSeparated[2])

#Q3
# values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
# numberOfValues = len(values)
# total = sum(values)
# average = (total/numberOfValues)
# print(values)
# print("We have",(numberOfValues),"values")
# print("Total is:",total)
# print("Average is:","%0.0f" %average,"(That being the above total divided by the number of values (",(numberOfValues),"))")
# print("The highest number is:",max(values))

#Q4
Name = input("What is your full name (including any middle names)? ")
FullName = Name.split()
Initials = ""
for placement in range (len(FullName)):
    Initials+=FullName[placement][0]
print("Full name:",Name)
print("Initials:",Initials)

#Q5
# numbers = list(input("Enter a number (type x to stop):")
# placement = 0
# while numbers[-0] != "x":
#     numbers.append = input("Enter a number (type x to stop):")
# print("You entered:",numbers)

#Q6
# Write a program that asks the user for a large number, and then sums all of the digits in that number: Example:
# Enter a large number: 29834892
# Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45 
 
#Q7
# Write a program to ask the user for numbers, and then print any repeating numbers in a list. Example:
# Enter a number: 5
# Enter a number: 2
# Enter a number: 6
# Enter a number: 98
# Enter a number: 7
# Enter a number: 6
# Enter a number: 5
# Enter a number: x
# Repeating numbers: [5, 6]