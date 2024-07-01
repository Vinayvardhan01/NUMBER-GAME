import random  # Import the random module

# Generate a random 4-digit number
random_num = random.randint(1000, 9999)
# print(random_num)

# Get user input
n = int(input("Enter a 4-digit number: "))

while n != 10:
    num = random_num  # This is for reading individual digits in the random number
    correct = 0
    temp_n = n  # This is for reading individual digits in the user's number

    for _ in range(4):
        numc = num % 10
        nc = temp_n % 10
        num = num // 10
        temp_n = temp_n // 10
        if numc == nc:
            correct += 1  # Correct should be increased if the digits are equal

    if correct == 4:
        print("Congrats: you guessed it right!")
        break
    else:
        print("%d digits were guessed right", correct)
        n = int(input("Enter a 4-digit number: "))
else:
    print("Thanks for playing")
