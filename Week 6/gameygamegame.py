#Setting initial parameters
print("Hey there! Let's play a little guessing game:")
#This is the correct answer we want the user to give
answer = int(17)
#This is the allowed number of guesses
allowedGuesses = int(7)
#This is setting guess as an array
guesses = []
#This is setting our counter
counter = int(0)
while True:
    #Asking for first guess
    guess = int(input("Guess the number between 0 and 25: "))
    #creating list
    guesses.append(guess) 
    #Giving hints to user to narrow down guesses
    if (guess == answer):
        print("The number was indeed "+str(guess)+"!")
        print("You guessed in "+str(counter+1)+" guesses.")
        print("Your guess log: "+str(guesses))
        break
    elif (guess < answer):
        print("Nope, it's greater than that.")
    elif (guess > answer):
        print("Nope, it's less than that.")
    print("You have "+str(7-counter)+" guesses left!")  
    #Counting down the guesses by iterating the loop
    counter += 1
    #For when the counter reaches 7
    if counter == 7:
        print("AHAHAA YOU LOOSE!")
        print("The number was "+str(answer))
        print("Your guess log: "+str(guesses))
    
    