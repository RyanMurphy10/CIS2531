#######################################################################################
#Assgn_8 Ryan Murphy 
#sets a dictionary for the Morse code letter outputs
#creates a function that converts a letter string to Morse code
#creates vowel count and constant count functions
#code prompts the user to input a string
#code goes through the user's string and counts the vowels and constants
#code then separates the string by space and prints out the Morse code for each letter
#code then prints the morse code and the vowel and constant count for the string the user inputted
#######################################################################################
# initialize the morse code dictionary with the characters and their corresponding morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': 'space'
}

# Function to convert the user input to Morse code
def convert_to_morse_code(text):
    # Create an empty list to store the Morse code
    morse_code = []
    # Iterate through each character in the user input
    for char in text:
        # Convert the character to uppercase
        char = char.upper()
        # Check if the character is in the dictionary
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
    return ' '.join(morse_code)

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Convert the user input to Morse code
morse_code = convert_to_morse_code(user_input)

# Display the Morse code
print("Morse code:", morse_code)

# function to count the number of vowels and consonants in a string
def count_vowels_and_consonants(text):

    # Define a string of vowels
    vowels = 'AEIOU'
    # Initialize vowel and consonant counts
    vowel_count = 0
    consonant_count = 0

    # Count the number of vowels and consonants
    for char in text:
        # If the character is a vowel, increment the vowel count
        if char.upper() in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Count the number of vowels and consonants
vowel_count, consonant_count = count_vowels_and_consonants(user_input)

# Display the results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)