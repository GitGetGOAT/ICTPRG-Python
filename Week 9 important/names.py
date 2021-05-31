#creating loop
while True:
    #Opening file
    with open('people.txt', 'a') as file:
        #Asking for names, until they enter an empty name
        name=input("Enter a name (when finished entering names, just hit enter without typing anything): ")
        #creating ability to stop program
        if name == "":
            break 
        #adding name to file
        else:
            file.write(name+"\n")