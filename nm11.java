import java.util.Arrays;

/**
 * The nm11 class implements the Sieve of Eratosthenes algorithm
 * to efficiently find all prime numbers up to a specified limit N.
 *
 * It utilizes primitive boolean[] and int[] arrays for optimal
 * performance and minimal overhead, which is crucial for
 * large-scale computations.
 */
public class nm11 {
    /**
     * The main method serves as the entry point for the program.
     * It executes the Sieve of Eratosthenes algorithm to mark
     * and then count all prime numbers up to N, finally printing
     * the total count and the first 10 primes found.
     *
     * @param args Command line arguments. The first argument, if present,
     * is used to set the upper limit N for finding primes.
     * Defaults to 100,000,000.
     */
    public static void main(String[] args) {
        int N = 100000000;
        if (args.length > 0) {
            N = Integer.parseInt(args[0]);
        }

        boolean[] isPrime = new boolean[N + 1];
        for (int i = 0; i <= N; i++) {
            isPrime[i] = true;
        }

        isPrime[0] = false;
        isPrime[1] = false;

        int limit = (int) Math.sqrt(N);
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= N; j = j + i) {
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

        int[] primes = new int[count];
        int index = 0;
        for (int i = 2; i <= N; i++) {
            if (isPrime[i]) {
                primes[index] = i;
                index++;
            }
        }

        System.out.println("Liczb pierwszych do " + N + " jest: " + count);

        System.out.println("Pierwsze 10 liczb pierwszych:");
        for (int i = 0; i < 10 && i < primes.length; i++) {
            System.out.print(primes[i] + " ");
        }

        System.out.println();
        System.out.println("Koniec programu!");
    }
}