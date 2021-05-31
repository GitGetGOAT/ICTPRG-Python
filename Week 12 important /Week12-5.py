# Write the function between the START and END tags
# START
def IsPalindrome(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(" ","")
    text = phrase [::-1]
    return phrase == text


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))