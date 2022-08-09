#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[3]:


#define a function 
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))
#user input
nterms = int(input('Please enter number of terms:'))

#validate number of terms
if nterms <= 0:
    print('Please enter a positive integer:')
else:
    print('Fibonacci series:')
    for i in range(nterms):
        print(fibonacci_recursion(i))


# ### 2. Write a Python Program to Find Factorial of Number Using Recursion?

# In[4]:


def factorial_recursion(n):
    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1)
num= int(input('Please enter a number: '))
if num <= 0:
    print('Factorial does not exist for negative numbers')
elif num==0:
    print('Factorial of 0 is 1')
else:
    print('Factorial of', num , 'is', factorial_recursion(num))


# ### 3. Write a Python Program to calculate your Body Mass Index?

# In[2]:


height = float(input('Enter height of a person in cm: '))
weight = float(input('Enter weight of a person in kg: '))
BMI = weight / (height/100)**2  #dividing by 100 so that we can get height in meters
print('Your Body Mas index is',BMI)

if BMI <= 18.5:
    print('Oops! You are underwieght')
elif BMI <= 24.9:
    print('Awesome! You are healthy')
elif BMI <=29.9:
    print('You are overweight')
else:
    print('You are obese')


# ### 4. Write a Python Program to calculate the natural logarithm of any number?

# In[3]:


import math 

number = int(input('Enter a number: '))
ans = math.log(number)
print('The value is:',ans)


# ### 5. Write a Python Program for cube sum of first n natural numbers?

# In[5]:


num = int(input('Enter a number: '))
sum = 0
for i in range(num+1):
    sum += i**3
    
print('The sum of cube of first',num,'natural number is',sum)

