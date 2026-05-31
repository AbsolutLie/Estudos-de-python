#!/usr/bin/env python 
"""Este programa exibe quantos números primos existem dentro de um i
de números naturais definido pelo usuário. Além disso, ele calcula 
a proporção de números primos em relação ao todo
"""

__version__ = "0.1.0"
__author__ = "Matheus"

#This function defines what is a prime number
def is_prime(n):
    is_prime = True
    number = int(n)
    for d in range(2,number):
        if int(n) % d == 0:
            is_prime = False
            break
    return is_prime

#This counts the number of primes less than n
def Tauberian(n):
    number = int(n)
    primes = 0
    for i in range(1,number):
        if is_prime(i):
            primes = primes + 1
    return primes

print("pick your number:")
num = input()
print(Tauberian(num))




            

        
