# znajdź liczby pierwsze do 10 milionów
import sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000000  
isPrime = [True] * (N + 1)  # tablica logiczna

# 0 i 1 nie są liczbami pierwszymi
isPrime[0] = False
isPrime[1] = False

# tylko do pierwiastka z N
limit = int(N ** 0.5)

# sito Eratostenesa
for i in range(2, limit + 1):
    if isPrime[i]:  # jeśli liczba jest pierwsza
        # wykreślamy wszystkie jej wielokrotności
        for j in range(i * i, N + 1, i):
            isPrime[j] = False

# zapisujemy i liczymy liczby pierwsze
primes = []   # lista do przechowywania liczb pierwszych
count = 0

for i in range(2, N + 1):
    if isPrime[i]:
        primes.append(i)
        count += 1

print(f"Liczb pierwszych do {N} jest: {count}")

# przykład: wypisz pierwsze 10 liczb pierwszych
print("Pierwsze 10 liczb pierwszych:", primes[:10])
