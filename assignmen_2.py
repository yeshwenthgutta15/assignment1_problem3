#Write a Python program that accepts a word from the user and reverse it

# take input from the user
value = input('Enter the word or name: ')
print('The input word is:',value)
str1 = ''
# for loop starts from here
for i in value:   
    str1 = i + str1 
print('The output is:',str1)
