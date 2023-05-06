#Write a Python program to count the number of even and odd numbers from a series of numbers.

# takeing input from the user 

numb1 = input("Enter a list of numbers, separated by spaces: ").split()

# Convert the list of strings to the integers (int format)
numb1 = [int(num) for num in numb1]

even_count = 0
odd_count = 0

# for loop starts from here
for num in numb1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
