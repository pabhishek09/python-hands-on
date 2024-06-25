def get_digits(number):
    """Given an int or string, return a list of digits in it."""
    string = str(number)
    return [x for x in string if x.isdigit()]

def main():
    s = input("Enter something: ")
    digits = get_digits(s)
    print("Digits found:", digits)
    if digits != []:
        main()

# Call main() if and only if started from this file
if __name__ == '__main__':
    main()
