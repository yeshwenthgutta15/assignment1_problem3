# Write a python program to get the febonacci series between 0 to 50

n = int(input("Enter the value of 'n':" ""))
num = 10
n1, n2 = 0, 1
print("Fibonacci Series : ", n1, n2, end = " ")
#for loops start from now
for i in range (2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end = " ")

    print()