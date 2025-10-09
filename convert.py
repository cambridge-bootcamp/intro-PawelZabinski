import sys

def convert_to_binary(number: int) -> str:
    # Convert the integer to a binary string e,g, 20 should give '10100'

    result: str = ""

    while number > 0:
        result += str(number % 2)
        number //= 2
    
    return result[::-1]
    

def main() -> None:
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
        
    input_arg: str = sys.argv[1]
    try:
        number: int = int(input_arg)
    except ValueError:
        print(f"Please supply a valid integer as input")
        exit(-1)
          
    binary_representation: str = convert_to_binary(number)

    print(f"The binary representation of {input_arg} is: {binary_representation}")

if __name__ == "__main__":
    main()
