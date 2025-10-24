#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

/**
 * The main function serves as the entry point for the program.
 * It implements the Sieve of Eratosthenes algorithm using dynamic
 * C-style arrays (pointers) to efficiently find all prime numbers
 * up to a specified limit N.
 *
 * It takes the upper limit N as an optional command-line argument.
 *
 * @param argc The number of command-line arguments.
 * @param argv An array of command-line arguments. argv[1] is the limit N.
 * @return Returns 0 upon successful completion.
 */
int main(int argc, char* argv[]) {
    int N = 100000000;
    if (argc > 1) {
        N = atoi(argv[1]);
    }

    bool *isPrime = new bool[N + 1];

    for (int i = 0; i <= N; i++) {
        isPrime[i] = true;
    }

    isPrime[0] = false;
    isPrime[1] = false;

    int limit = sqrt(N);

    for (int i = 2; i <= limit; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= N; j += i) {
                isPrime[j] = false;
            }
        }
    }

    int count = 0;
    for (int i = 2; i <= N; i++) {
        if (isPrime[i]) {
            count++;
        }
    }

    int *primes = new int[count];
    int index = 0;

    for (int i = 2; i <= N; i++) {
        if (isPrime[i]) {
            primes[index] = i;
            index++;
        }
    }

    cout << "Liczb pierwszych do " << N << " jest: " << count << endl;

    cout << "Pierwsze 10 liczb pierwszych: ";
    for (int i = 0; i < 10 && i < count; i++) {
        cout << primes[i] << " ";
    }
    cout << endl;

    delete[] isPrime;
    delete[] primes;

    return 0;
}