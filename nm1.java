import java.util.ArrayList;

public class nm1 {
    public static void main(String[] args) {
        int N = 100000000; // sprawdzamy liczby do 100 milionów
        if (args.length > 0) {
            N = Integer.parseInt(args[0]);
        }

        // tworzymy tablice boolean - zakładamy że wszystkie liczby są pierwsze
        boolean[] isPrime = new boolean[N + 1];
        for (int i = 0; i <= N; i++) {
            isPrime[i] = true;
        }

        // 0 i 1 nie są liczbami pierwszymi
        isPrime[0] = false;
        isPrime[1] = false;

        // sito Eratostenesa
        int limit = (int) Math.sqrt(N); // wystarczy sprawdzać do pierwiastka z N

        for (int i = 2; i <= limit; i++) {
            if (isPrime[i] == true) { // jeśli liczba jest pierwsza
                // usuwamy wszystkie jej wielokrotności
                for (int j = i * i; j <= N; j = j + i) {
                    isPrime[j] = false; // oznaczamy jako niepierwsze
                }
            }
        }

        // liczymy i zapisujemy liczby pierwsze
        int count = 0;
        ArrayList<Integer> primes = new ArrayList<>();

        for (int i = 2; i <= N; i++) {
            if (isPrime[i] == true) {
                count++;
                primes.add(i); // dodajemy liczbe pierwsza do listy
            }
        }

        System.out.println("Liczb pierwszych do " + N + " jest: " + count);

        // wypisujemy pierwsze 10 liczb pierwszych jako przykład
        System.out.println("Pierwsze 10 liczb pierwszych:");
        for (int i = 0; i < 10 && i < primes.size(); i++) {
            System.out.print(primes.get(i) + " ");
        }

    }
}
