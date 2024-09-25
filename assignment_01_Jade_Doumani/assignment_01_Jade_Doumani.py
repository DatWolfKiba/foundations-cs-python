""" #Excercise 1 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print("The biggest number is " + str(a))
elif b >= a and b >= c:
    print("The biggest number is " + str(b))
else:
    print("The biggest number is " + str(c))

#Excercise 2 

#I had to use try and except, even though we didn't learn it yet, in case you tried to use a value that isn't an int
try:
    n = int(input("Johnny, please insert a positive integer: "))
    product = 1
    found_odd = False 

    if n > 0:
        for integers in range(1, n + 1):
            if integers % 2 != 0:
                found_odd = True
                product *= integers
                if product > 100:
                    print("Multiplication exceeded, Johnny!")
                    break
        else:
            if found_odd:
                print("Product of odd numbers:", product)
            else:
                print("1")
    elif n < 0: 
        print("You did not use a positive integer, Johnny!")

except ValueError:
    print("You didn't even use an integer, Johnny!")

#Excercise 3 
scores = 0
fullScore = 0
counter = 0

while scores != -1:
    try:
        scores = float(input("Enter the score here, Johnny, or enter -1 to calculate the average: "))
        if scores != -1:
            fullScore += scores
            counter += 1
    except ValueError:
        print("Please enter a valid integer, Johnny!")

if counter == 0:
    print("No valid scores were entered, Johnny!")
else:
    average = round((fullScore / counter), 1) #I needed to use the round() function so that I can get the first decimal only
    print(f"Average score: " + str(average))

#Excercise 4 

try:
    ABCD = int(input("Enter a four-digit number, Johnny: "))
except ValueError:
    print("Please enter a valid integer, Johnny!")

if ABCD < 1000 or ABCD > 9999:
    print("You didn't enter a four-digit number, Johnny!")
else:
    A = ABCD // 1000
    B = (ABCD // 100) % 10
    C = (ABCD // 10) % 10
    D = ABCD % 10
    if (A + B) == (C + D):
        print("F")
    else:
        print("U") """