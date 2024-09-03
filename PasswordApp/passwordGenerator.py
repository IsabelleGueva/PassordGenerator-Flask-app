#8-25-2024 
#create a password 6-8 characters long
#password requirements:
#at least 1 number
#at least 1 symbol (!@#$%^&*)
#at least 1 capital letter
import random
import string

symbolsList = ['!', '@', '#', '$', '%', '^', '&', '*']

def checkRequirements(possiblePass, upperCheck, numberCheck, symbolCheck):
    upperMet = False
    numberMet = False
    symbolMet = False
    for element in possiblePass:
        if element.isupper():
            upperMet = True
        elif element.isnumeric():
            numberMet = True
        elif element in symbolsList:
            symbolMet = True
    return upperMet==upperCheck and numberMet==numberCheck and symbolCheck==symbolMet
def addRandomly(element, base_password):
        new_spot = random.randrange(0, len(base_password)-1)
        firstPart = base_password[:new_spot]
        lastPart = base_password[new_spot:]
        new_password = firstPart + str(element) +lastPart
        return new_password

def generatePassword(length, nums, uppers, symbolVal):
    symbols = ''.join(symbolsList)
    characters = string.ascii_lowercase
    if nums:
        characters += string.digits
    if uppers:
        characters += string.ascii_uppercase
    if symbolVal:
        characters += symbols

    while True:
        result = ''.join(random.choices(characters, k=length))
        if checkRequirements(result, uppers, nums, symbolVal):
            return result

