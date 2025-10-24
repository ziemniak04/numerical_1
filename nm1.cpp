#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

/**
 * The main function serves as the entry point for the program.
 * It implements the Sieve of Eratosthenes algorithm using a C-style
 * dynamic array (bool*) for the sieve flags and a C++ standard library
 * vector (std::vector<int>) to store the resulting prime numbers.
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

    vector<int> primes;
    int count = 0;

    for (int i = 2; i <= N; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
            count++;
        }
    }

    cout << "Liczb pierwszych do " << N << " jest: " << count << endl;

    cout << "Pierwsze 10 liczb pierwszych: ";
    for (int i = 0; i < 10 && i < primes.size(); i++) {
        cout << primes[i] << " ";
    }
    cout << endl;

    delete[] isPrime;

    return 0;
}