import sys

def convert_to_ternary(number):
    # Convert the integer to a binary string e,g, 20 should give '10100'

    result = ""

    while number > 0:
        result += str(number % 3)
        number //= 3
    
    return result[::-1]
    

def main():
    """
    Main function to handle command-line arguments and run the conversion.
    """
    # sys.argv is a list containing the script name and its arguments.
    # We expect two items: the script name itself (at index 0) and
    # one argument (at index 1).
    if len(sys.argv) != 2:
        print("Usage: python int_to_binary.py <integer>")
        # Exit the script with a status code of 1 to indicate an error
        sys.exit(1)
        
    input_arg = sys.argv[1]
    try:
        number = int(input_arg)
    except ValueError:
        print(f"Please supply a valid integer as input")
        exit(-1)
          
    binary_representation = convert_to_ternary(number)

    print(f"The ternary representation of {input_arg} is: {binary_representation}")

if __name__ == "__main__":
    main()
