user_input = input('Enter the numnber:')

if not user_input.isnumeric():
    print('Invalid input')
    exit()


def prime_number(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            print('Not a prime number, divisible by', i)
            return False
        
    print('Prime number')
    return True

print(prime_number(int(user_input)))
