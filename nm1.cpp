/**
 * @file nm1.cpp
 * @brief Sieve of Eratosthenes implementation for finding prime numbers.
 * 
 * This program finds all prime numbers up to a given limit N using the Sieve of Eratosthenes
 * algorithm. The limit can be provided as a command-line argument or defaults to 100,000,000.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

/**
 * @brief Implements the Sieve of Eratosthenes algorithm.
 * 
 * @param n The upper limit for finding prime numbers
 * @return A boolean array where isPrime[i] is true if i is prime
 */
bool* sieveOfEratosthenes(int n) {
    bool* isPrime = new bool[n + 1];
    
    for (int i = 0; i <= n; i++) {
        isPrime[i] = true;
    }
    
    isPrime[0] = false;
    isPrime[1] = false;
    
    int limit = sqrt(n);
    
    for (int i = 2; i <= limit; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    return isPrime;
}

/**
 * @brief Collects all prime numbers from the sieve result.
 * 
 * @param isPrime Boolean array indicating which numbers are prime
 * @param n The upper limit that was checked
 * @return Vector containing all prime numbers up to n
 */
vector<int> collectPrimes(bool* isPrime, int n) {
    vector<int> primes;
    
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }
    
    return primes;
}

/**
 * @brief Prints the results including total count and first 10 prime numbers.
 * 
 * @param n The upper limit that was checked
 * @param primes Vector of all prime numbers found
 */
void printResults(int n, const vector<int>& primes) {
    cout << "Liczb pierwszych do " << n << " jest: " << primes.size() << endl;
    
    cout << "Pierwsze 10 liczb pierwszych: ";
    for (int i = 0; i < 10 && i < primes.size(); i++) {
        cout << primes[i] << " ";
    }
    cout << endl;
}

/
