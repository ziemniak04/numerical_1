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
    # Use a bytearray for memory efficiency: 1 byte per flag (1 = prime candidate, 0 = not prime)
    isPrime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        isPrime[0] = 0
    if n >= 1:
        isPrime[1] = 0

    limit = int(n ** 0.5)

    for i in range(2, limit + 1):
        if isPrime[i]:
            step = i
            start = i * i
            # mark multiples as non-prime (0)
            for j in range(start, n + 1, step):
                isPrime[j] = 0

    # Collect primes
    primes = [i for i in range(2, n + 1) if isPrime[i]]
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
