import re

def validate_phone_number(phone_number):

    #Validate phone number in the format (123) 456-7890

    #Args: phone_number (str): Phone number to validate

    #Returns: bool: True if valid, False otherwise

    # Define the regex pattern for phone number
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    # Check if the phone number matches the pattern
    return bool(pattern.match(phone_number))

def validate_ssn(ssn):

    #Validate social security number in the format 123-45-6789

    #Args: ssn (str): Social security number to validate

    #Returns: bool: True if valid, False otherwise

    # Define the regex pattern for SSN
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    # Check if the SSN matches the pattern
    return bool(pattern.match(ssn))

def validate_zip_code(zip_code):

    #Validate zip code in the format 12345 or 12345-6789

    #Args: zip_code (str): Zip code to validate

    #Returns: bool: True if valid, False otherwise

    # Define the regex pattern for zip code
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    # Check if the zip code matches the pattern
    return bool(pattern.match(zip_code))

def main():

    #Main function to get user input and validate phone number, social security number, and zip code.

    # Get user input for phone number
    phone_number = input("Enter phone number (format: (123) 456-7890): ")
    # Get user input for social security number
    ssn = input("Enter social security number (format: 123-45-6789): ")
    # Get user input for zip code
    zip_code = input("Enter zip code (format: 12345 or 12345-6789): ")

    # Validate the phone number and print the result
    if validate_phone_number(phone_number):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    # Validate the social security number and print the result
    if validate_ssn(ssn):
        print("Social security number is valid.")
    else:
        print("Social security number is invalid.")

    # Validate the zip code and print the result
    if validate_zip_code(zip_code):
        print("Zip code is valid.")
    else:
        print("Zip code is invalid.")

if __name__ == "__main__":
    main()