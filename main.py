import sys  # Importing the sys module for system-related operations
import json  # Importing the json module for JSON data processing

class TextEncryptor:  # Defining a class named TextEncryptor
    def __init__(self):  # Constructor method of the class
        self.encryption_table = self.load_encryption_table()  # Loading the encryption table

    def load_encryption_table(self):  # Defining a method to load the encryption table
        try:  # Starting error handling
            with open('encryption_table.json', 'r') as file:  # Reading the encryption_table.json file
                encryption_table = json.load(file)  # Reading the data from the file and assigning it to the encryption_table variable
        except FileNotFoundError:  # Handling the file not found error
            print("Encryption table not found. Creating a new table...")  # Informing the user
            encryption_table = {}  # Creating an empty encryption table
        return encryption_table  # Returning the created or loaded encryption table

    def save_encryption_table(self):  # Defining a method to save the encryption table
        with open('encryption_table.json', 'w') as file:  # Opening the encryption_table.json file for writing
            json.dump(self.encryption_table, file, indent=4)  # Writing the encryption table to the file

    def encrypt(self, text):  # Defining a method to encrypt text
        encrypted_text = ""  # Creating an empty string to hold the encrypted text
        for char in text:  # Iterating over each character in the text
            if char in self.encryption_table:  # If the character is found in the encryption table
                encrypted_text += self.encryption_table[char] + " "  # Adding the character's code to the encrypted text
            else:  # If the character is not found in the encryption table
                encrypted_text += char  # Adding the character directly to the encrypted text
        return encrypted_text  # Returning the encrypted text

    def decrypt(self, text):  # Defining a method to decrypt text
        decrypted_text = ""  # Creating an empty string to hold the decrypted text
        codes = text.split()  # Splitting the encrypted text by spaces to get the codes into a list
        for code in codes:  # Iterating over each code
            found = False  # Flag to indicate if the corresponding character is found
            for key, value in self.encryption_table.items():  # Iterating over each item in the encryption table
                if code == value:  # If the code matches a value in the encryption table
                    decrypted_text += key  # Adding the corresponding character to the decrypted text
                    found = True  # Marking as found
                    break  # Exiting the loop
            if not found:  # If no corresponding character is found for the code
                decrypted_text += code  # Adding the code directly to the decrypted text
        return decrypted_text  # Returning the decrypted text

    def add_or_update_entry(self, character, code):  # Defining a method to add or update an entry in the encryption table
        self.encryption_table[character] = code  # Adding the character and its corresponding code to the encryption table
        self.save_encryption_table()  # Saving the encryption table
        print(f"Entry added or updated for character '{character}' with code '{code}'.")  # Informing the user

def main():  # Defining the main function
    encryptor = TextEncryptor()  # Creating an instance of the TextEncryptor class

    # Display coder's information and GitHub link
    print("\nCoded by H0dg4m")
    print("GitHub: https://github.com/h0dg4m")  
    
    while True:  # Starting an infinite loop
        print("\n1 - Encrypt Text\n2 - Decrypt Text\n3 - Add or Update Encryption Code\n4 - Exit")  # Printing the menu options
        choice = input("Your choice: ")  # Asking the user for choice

        if choice == '1':  # If the user chooses option 1
            input_text = input("Enter the text to encrypt: ")  # Taking input text from the user
            encrypted_text = encryptor.encrypt(input_text)  # Encrypting the text
            print("Encrypted text:", encrypted_text)  # Printing the encrypted text
        elif choice == '2':  # If the user chooses option 2
            input_text = input("Enter the text to decrypt: ")  # Taking input text from the user
            decrypted_text = encryptor.decrypt(input_text)  # Decrypting the text
            print("Decrypted text:", decrypted_text)  # Printing the decrypted text
        elif choice == '3':  # If the user chooses option 3
            character = input("Enter the new character: ")  # Taking the new character from the user
            code = input("Enter the encryption code for the character: ")  # Taking the encryption code from the user
            encryptor.add_or_update_entry(character, code)  # Adding or updating the encryption entry
        elif choice == '4':  # If the user chooses option 4
            print("\nCoded by H0dg4m")
            print("Exiting the program...")  # Saying goodbye to the user
            break  # Exiting the infinite loop, terminating the program
        else:  # If an invalid choice is entered
            print("Invalid choice. Please try again.")  # Informing the user

if __name__ == "__main__":  # If this file is run directly
    main()  # Calling the main function


# Coded by H0dg4m
# GitHub: https://github.com/h0dg4m
