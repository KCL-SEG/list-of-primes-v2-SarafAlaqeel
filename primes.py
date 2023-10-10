"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkprime(num):

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    else:
        return False

def primes(number_of_primes):
    list = []
    num =2
    if number_of_primes <= 0:
        raise ValueError("The number must be a positive integer greater than zero")

    while len(list) < number_of_primes:
        if(checkprime(num)):
           list.append(num)
        num = num +1
    return list

