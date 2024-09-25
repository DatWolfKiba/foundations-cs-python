''' #Exercise 1
def factorial(n):
    if n < 0:
        return "Negative numbers have no factorials."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

n = int(input("Enter number: "))
print("The factorial of", n, "is", factorial(n))

#Exercise 2

def find_divisors(n):
    if n <= 0:
        return "Enter a positive integer."
    
    divisors = []
   
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    return divisors


n = int(input("Enter number: "))
print("The divisors of", n, "are:", find_divisors(n))

#Exercise 3

def reverseString(s):
    
    reversed_string = ""
    
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    
    return reversed_string

s = input("Enter a string: ")
print("The reversed string is:", reverseString(s))'''

'''def find_even_numbers(numbers):
    even_numbers = []  
    
    for num in numbers:
        if num % 2 == 0:  
            even_numbers.append(num)  
    
    return even_numbers  

numbers = input("Enter a list of integers (separated by spaces): ").split()

int_numbers = []
for num in numbers:
    int_numbers.append(int(num))  

print("The even numbers are:", find_even_numbers(int_numbers))

#Exercise 4

def check_password_strength(password):
    
    if len(password) < 8:
        return "Weak password"
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "#?!$":
            has_special = True
    
    if has_upper and has_lower and has_digit and has_special:
        return "Strong password"
    else:
        return "Weak password"
    
password = input("Enter a password: ")
print(check_password_strength(password))

#Exercise 5

def is_valid_ipv4(address):

    octets = address.split('.')
    
    if len(octets) != 4:
        return "Invalid IPv4 address"
    
    for octet in octets:
        try:

            num = int(octet)
        except ValueError:
            return "Invalid IPv4 address"  # Not a valid integer

        if num < 0 or num > 255 or (octet != '0' and octet.startswith('0')):
            return "Invalid IPv4 address"
    
    return "Valid IPv4 address"

address = input("Enter an IPv4 address: ")
print(is_valid_ipv4(address))'''

