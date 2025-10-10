#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[]) {
    int N = 100000000; // znajdź liczby pierwsze do 100 milionów
    if (argc > 1) {
        N = atoi(argv[1]);
    }
    bool *isPrime = new bool[N + 1]; // tablica logiczna

    // zakładamy, że wszystkie liczby są pierwsze
    for (int i = 0; i <= N; i++) {
        isPrime[i] = true;
    }

    // 0 i 1 nie są pierwsze
    isPrime[0] = false;
    isPrime[1] = false;

    // tylko do pierwiastka z N
    int limit = sqrt(N);

    // sito Eratostenesa
    for (int i = 2; i <= limit; i++) {
        if (isPrime[i]) { // jeśli i jest pierwsze
            // wykreślamy wielokrotności i
            for (int j = i * i; j <= N; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // zapisujemy liczby pierwsze do wektora i liczymy
    vector<int> primes;
    int count = 0;

    for (int i = 2; i <= N; i++) {
        if (isPrime[i]) {
            primes.push_back(i); // dodajemy do listy
            count++;             // zwiększamy licznik
        }
    }

    cout << "Liczb pierwszych do " << N << " jest: " << count << endl;

    // przykład: wypisz pierwsze 10 liczb pierwszych
    cout << "Pierwsze 10 liczb pierwszych: ";
    for (int i = 0; i < 10 && i < primes.size(); i++) {
        cout << primes[i] << " ";
    }
    cout << endl;

    delete[] isPrime; // sprzątamy pamięć

    return 0;
}
