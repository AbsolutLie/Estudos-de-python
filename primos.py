#!/usr/bin/env python 
"""Este programa exibe quantos números primos existem dentro de um intervalo
de números naturais definido pelo usuário. Além disso, ele calcula 
a proporção de números primos em relação ao todo.
"""

__version__ = "0.1.0"
__author__ = "Matheus"

import time
import math
import sys

# Raise the recursion limit from 1,000 to 20,000
sys.setrecursionlimit(20000)

class PrimeCounter:
    def __init__(self):
        self.primes = []
        self.phi_cache = {}

    def _sieve(self, limit):
        """A tiny, fast Sieve just to find primes up to the square root."""
        if limit < 2:
            self.primes = []
            return
            
        sieve = bytearray(b'\x01') * (limit + 1)
        sieve[0] = 0
        sieve[1] = 0
        for p in range(2, int(limit**0.5) + 1):
            if sieve[p]:
                sieve[p*p : limit+1 : p] = bytearray(b'\x00') * len(range(p*p, limit+1, p))
        self.primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    def _phi(self, x, a):
        """The recursive partial sieve function."""
        # Base cases
        if a == 0:
            return int(x)
        if x == 0:
            return 0
            
        # Check our cache to see if we already did this math
        if x < 100000:
            if (x, a) in self.phi_cache:
                return self.phi_cache[(x, a)]
        
        # THE FIX: Use // for integer division here!
        result = self._phi(x, a - 1) - self._phi(x // self.primes[a - 1], a - 1)
        
        # Save to cache
        if x < 100000:
            self.phi_cache[(x, a)] = result
            
        return result

    def tauberian_legendre(self, n):
        """The main function to replace your Tauberian(n)."""
        number = int(n)
        
        # We want primes strictly less than n (based on your original code)
        number -= 1 
        
        if number < 2:
            return 0
            
        # 1. Find primes up to the square root of n
        limit = int(number**0.5)
        self._sieve(limit)
        
        # 2. 'a' is the count of those small primes
        a = len(self.primes)
        
        # 3. Apply Legendre's formula
        return self._phi(number, a) + a - 1

# Counts positive integers <= n that are NOT multiples of the first m given primes.
def sieve(m, n):
    first_primes_count = int(m)
    given = int(n)
    
    if given < 1 or first_primes_count < 1:
        return 0
        
    # 1. Find the first 'm' primes using a bounded Sieve
    primes_to_check = []
    
    # We use a fixed limit for small numbers because ln(ln(m)) breaks for m < 6
    if first_primes_count < 6:
        limit = 15 
    else:
        # Rosser's Theorem to find the maximum possible value of the m-th prime
        limit = int(first_primes_count * (math.log(first_primes_count) + math.log(math.log(first_primes_count)))) + 2
        
    # Run the Sieve up to our calculated limit
    is_prime_list = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime_list[p]:
            primes_to_check.append(p)
            
            # Stop exactly when we have our m primes
            if len(primes_to_check) == first_primes_count:
                break
                
            # Mark multiples as False
            for i in range(p * p, limit + 1, p):
                is_prime_list[i] = False
                
    # 2. Sieve the array up to 'n'
    not_multiples = [True] * (given + 1)
    not_multiples[0] = False 
    
    for p in primes_to_check:
        for i in range(p, given + 1, p):
            not_multiples[i] = False
            
    return sum(not_multiples)

print("Choose one of the following options:")
print("1. Compute if a given number is prime.")
print("2. Compute the number of primes strictly less than a given number.")
print("3. Given numbers m, n with m < n, compute the proportion between the number of primes up until n and the number of positive integers <= n that are not multiple of the first m primes.")
print("4. Given numbers m, n, compute ONLY the number of positive integers <= n that are not multiples of the first m primes.")

option = input("> ")

if option == "1":
    print("Choose a number:")
    num = input("> ")
    start = time.time()
    print(f"Is prime: {is_prime(num)}")
    end = time.time()
    print("Total estimated time:", end - start)

elif option == "2":
    print("Choose a number:")
    num = input("> ")
    start = time.time()
    
    # 1. Create an instance of the class
    calculator = PrimeCounter() 
    
    # 2. Call the method using the instance you just created
    primes_counted = calculator.tauberian_legendre(num)
    
    print(f"Total primes: {primes_counted}")
    end = time.time()
    print("Total estimated time:", end - start)

elif option == "3":
    print("Choose two numbers:")
    num_1 = input("m (number of primes): ")
    num_2 = input("n (upper limit): ")
    
    start = time.time()
    
    # Get the components
    not_multiple_count = sieve(num_1, num_2)
    
    # Instantiate the class and calculate primes
    calculator = PrimeCounter()
    prime_count = calculator.tauberian_legendre(num_2)
    
    print(f"Primes < {num_2}: {prime_count}")
    print(f"Numbers <= {num_2} not multiples of first {num_1} primes: {not_multiple_count}")
    
    # Calculate proportion (protect against division by zero)
    num_1_int = int(num_1) 
    
    if (num_1_int + not_multiple_count) == 0:
        print("Proportion: Undefined (division by zero)")
    else:
        print(f"Proportion: {prime_count / (num_1_int + not_multiple_count)}")
        
    end = time.time()
    print("Total estimated time:", end - start)

elif option == "4":
    print("Choose two numbers:")
    num_1 = input("m (number of primes): ")
    num_2 = input("n (upper limit): ")
    
    start = time.time()
    
    # Only run the sieve function
    not_multiple_count = sieve(num_1, num_2)
    
    print(f"Numbers <= {num_2} not multiples of first {num_1} primes: {not_multiple_count}")
        
    end = time.time()
    print("Total estimated time:", end - start)

else:
    print("Invalid option selected.")