# Code
from random import choice
from random import randint,sample,shuffle
import random,re
import string
print("This is the randaom password Generator")
print('''Example :
            no. of elements = 7
            i.e; to crteate random password ''')
n0 = int(input("Enter number of elements not less than 6 : "))
n1 = int(input("Enter the no. of Uppercase : "))
n2 = int(input("Enter the no. of Lowercase : "))
n3 = int(input("Enter the no. of special character : "))
word1 = string.ascii_uppercase
x = re.findall('[A-Z][^A-Z]*', word1) 
x1 = sample(x, k = n1)
word2 = string.ascii_lowercase
y = re.findall('[a-z][^a-z]*', word2)
y1 = sample(y, k = n2)
z = ['!', '@', '#', '$', '&', '*', '~']
z1 = sample(z, k = n3)
total = x1 + y1 + z1
shuffle(total)
print(total)
