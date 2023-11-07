############################################################################
#Assgn_4 Ryan Murphy
#User is prompted to enter a 16 digit credit card number
#The type of card is identified by the PrefixMatched function due to the first digits on the card
#The credit card is then identfied if it is valid throught the isValid function
#If the numbers do not match the card is determined to be unknown and Invalid
#The code is done reading the information after the credit card number is determined valid or invalid
############################################################################
def isValid(number):
    '''Return true if the card number is valid'''
    return (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0

def sumOfDoubleEvenPlace(number):
    '''Get the result from Step 2'''
    digits = [int(d) for d in str(number)][::-1]  # convert number to a list of digits in reverse order
    double_digits = [getDigit(2*d) for i, d in enumerate(digits) if i % 2 == 1]  # double every other digit starting from the second-to-last
    return sum(double_digits)

def getDigit(number):
    '''Return this number if it is a single digit, otherwise, return the sum of the two digits'''
    if number < 10: 
        return number #returns number if less than 10
    else:
        return number // 10 + number % 10 # if greater than returns sum of the two digits

def sumOfOddPlace(number):
    '''Return sum of odd place digits in number'''
    digits = [int(d) for d in str(number)][::-1]  #converts the numbers to a list of digits in reverse order
    return sum(digits[::2])  #adds the digits from the last spot and incriments on to each other

def prefixMatched(number, d):
    '''Return true if the digit d is a prefix for number'''
    return getPrefix(number, getSize(d)) == d;

def getSize(d):
    '''Return thhe number of digits in d'''
    return len(str(d)) #returns the length of the string of digits

def getPrefix(number, k):
    '''Return the first k number of digits from number. If the number of digits in number is less than k, return number'''
    return int(str(number)[:k]) #returns a string of numbers in reverse order, then converts it to a int

def main():
    '''Main function that takes in the other functions and prompts the user to input a card number and allows the code to run more smoothly'''
    Cardnumber = input("Input A Card Number: ") #input for the user
    
    if prefixMatched(Cardnumber, 4):
        print("Visa card") #prints "Visa" if input starts with 4
    elif prefixMatched(Cardnumber, 5):
        print("MasterCard credit card") #prints "MasterCard" if input starts with 5
    elif prefixMatched(Cardnumber, 37):
        print("American Express card")#prints "American Express card" if input starts with 37
    elif prefixMatched(Cardnumber, 6):
        print("Discover card") #prints "Discovery card" if input starts with 6
    else:
        print("Unknown card") #if card doesnt start with the numbers above "Unknown card" is printed
    
    if isValid(Cardnumber): #checks the isValid function to see if the card number is valid
        print("\nValid credit card number")
    else:
        print("\nInvalid credit card number")
      
if __name__ == "__main__":
  main()
