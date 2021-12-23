#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Joseph Krebs - sNNNNNNN"

# Write your functions here
lower_case_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_case_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def inputprompt():
    """ Return the user input when the user is asked what option they would like to use.

    Parameters:
        No parameters

    Return:
        str: selection from user input
    """
    selection = input("\nPlease choose an option [e/d/a/q]: \ne) Encrypt some text \nd) Decrypt some text \na) Automatically decrypt English text \nq) Quit \n")
    return selection

def decision(selection):
    """ Execute the function according to user selection, while also asking for text and offset where applicable.

    Parameters:
        selection: The program function selected by the user.

    Return:
        function: The function to be executed with relevant arguments.
    """
    if selection == 'e':
        text = str(input("Please enter some text to encrypt: "))
        offset = int(input("Please enter a shift offset(1-25): "))
        if offset >0:
            encryption_output = encrypt(text, offset)
            print("The encrypted text is:", encryption_output)
        else:
            i = 0
            print("The encrypted text is:\n")
            while i<26:
                encryption_output = encrypt(text, i)
                print(i,":",encryption_output)
                i+=1
    elif selection == 'd':
        text = str(input("Please enter some text to decrypt: "))
        offset = int(input("Please enter a shift offset(1-25): "))
        decryption_output = decrypt(text,offset)
        if offset > 0:
            decryption_output = decrypt(text, offset)
            print("The decrypted text is:", decryption_output)
        else:
            i = 0
            print("The decrypted text is:\n")
            while i<26:
                decryption_output = decrypt(text, i)
                print(i,":",decryption_output)
                i+=1

    elif selection == 'a':
        encrypted_text = str(input("Please enter some encrypted text: "))
        stored_offsets = find_encryption_offsets(encrypted_text)

        if len(stored_offsets) == 1:
            decrypted_text = decrypt(encrypted_text, stored_offsets[0])
            print("Encryption offset: ", stored_offsets[0])
            print("Decrypted message: ", decrypted_text)
        elif len(stored_offsets) > 1:
            print("Multiple encryption offsets:", stored_offsets)

        else:
            print("No valid encryption offset")
    elif selection == 'q':
        quitfunction()
    else:
        print("Invalid command!")

def encrypt(text,offset):
    """ Encrypt the text using the provided offset

    Parameters:
        text: text provided by the user in decision()
        offset: shift offset provided by the user in decision()
    Return:
        str: encrypted text 
    """
    encryption_output = ""
    space = False
    for i in range(0, len(text)):
        letter_number = 0

        letter_counter = 0
        for letter in lower_case_alphabet:
            
            if text[i] == letter:
                letter_number = letter_counter
            letter_counter += 1

            if text[i] == " ":
                space = True
            else:
                space = False
        for letter in upper_case_alphabet:
            
            if text[i] == letter:
                letter_number = letter_counter
            letter_counter += 1

            if text[i] == " ":
                space = True
            else:
                space = False



        encoded_number = offset + letter_number
        if text[i].isalpha() == False:
            if text[i] != "-":
                encryption_output += text[i]
            else:
                encryption_output += " "
        elif space != True:
            encryption_output += lower_case_alphabet[encoded_number % 26]
        else:
            encryption_output += " "

    return encryption_output

def decrypt(text,offset):
    """ Decrypt the text using the provided offset

    Parameters:
        text: text provided by the user in decision()
        offset: shift offset provided by the user in decision()
    Return:
        str: decrypted text
    """
    decryption_output = ""
    space = False
    for i in range(0, len(text)):
        letter_number = 0

        letter_counter = 0
        for letter in lower_case_alphabet:

            if text[i] == letter:
                letter_number = letter_counter
            letter_counter += 1

            if text[i] == " ":
                space = True
            else:
                space = False
        for letter in upper_case_alphabet:
            
            if text[i] == letter:
                letter_number = letter_counter
            letter_counter += 1

            if text[i] == " ":
                space = True
            else:
                space = False

        encoded_number = -offset + letter_number
        
        if text[i].isalpha() == False:
            if text[i] != "-":
                decryption_output += text[i]
            else:
                decryption_output += " "
            
        elif space!= True:
            decryption_output += lower_case_alphabet[encoded_number % 26]
        
        else:
            decryption_output += " "
    return decryption_output
    
def find_encryption_offsets(encrypted_text):
    """ Find the encryption offset of the provided text

    Parameters:
        encrypted_text: the encrypted text provided by the user
    Return:
        int: The possible shift offsets of the encrypted text
    """
    encrypted_text = encrypted_text.split(" ")
    stored_offsets = []
    for offset in range(1, 26):
        word = decrypt(encrypted_text[0], offset)
        if is_word_english(word) == True:
            stored_offsets.append(offset)
            if is_word_english(word) == False:
                    stored_offsets.remove(offset)
        for word in encrypted_text:
            for offset in stored_offsets:
                word = decrypt(word, offset)


    stored_offsets = tuple(stored_offsets)
    return stored_offsets


def quitfunction():
    """ Quit the program

    Parameters:
        None
    Return:
        Quits the program
    """
    print("Bye!")
    quit()
            
        
    


    
def main():
    """ The main execution line for the function

    Parameters:
        None
    Return:
        None
    """
    # Add your main code here
    print("\nWelcome to the simple encryption tool")
    while True:
        s = inputprompt()
        decision(s)
    pass


##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()

