"""
Sieve of Eratosthenes implementation for finding prime numbers.

This script finds all prime numbers up to a given limit N using the Sieve of Eratosthenes
algorithm. The limit can be provided as a command-line argument or defaults to 100,000,000.
"""

import sys


def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    
    Args:
        n (int): Upper limit for finding prime numbers
        
    Returns:
        list: List of all prime numbers up to n
    """
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    
    limit = int(n ** 0.5)
    
    for i in range(2, limit + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    
    primes = []
    for i in range(2, n + 1):
        if isPrime[i]:
            primes.append(i)
    
    return primes


def main():
    """
    Main function to execute the prime number finding algorithm.
    
    Reads N from command-line arguments or uses default value, finds all primes
    up to N, and prints the count and first 10 primes.
    """
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000000
    
    primes = sieve_of_eratosthenes(N)
    count = len(primes)
    
    print(f"Liczb pierwszych do {N} jest: {count}")
    print("Pierwsze 10 liczb pierwszych:", primes[:10])


if __name__ == '__main__':
    main()
