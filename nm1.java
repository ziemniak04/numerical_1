import java.util.ArrayList;

/**
 * The nm1 class implements the Sieve of Eratosthenes algorithm
 * to find all prime numbers up to a specified limit N.
 *
 * It uses an ArrayList<Boolean> for the sieve, demonstrating the
 * use of Java's dynamic collection framework for a large-scale
 * computation.
 */
public class nm1 {
    /**
     * The main method serves as the entry point for the program.
     * It performs the Sieve of Eratosthenes and prints the count
     * of prime numbers found, along with the first 10 primes.
     *
     * @param args Command line arguments. The first argument, if present,
     * is used to set the upper limit N for finding primes.
     * Defaults to 10,000,000.
     */
    public static void main(String[] args) {
        int N = 10000000;
        if (args.length > 0) {
            N = Integer.parseInt(args[0]);
        }

        ArrayList<Boolean> isPrime = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            isPrime.add(true);
        }

        isPrime.set(0, false);
        isPrime.set(1, false);

        int limit = (int) Math.sqrt(N);
        for (int i = 2; i <= limit; i++) {
            if (isPrime.get(i)) {
                for (int j = i * i; j <= N; j += i) {
                    isPrime.set(j, false);
                }
            }
        }

        ArrayList<Integer> primes = new ArrayList<>();

        for (int i = 2; i <= N; i++) {
            if (isPrime.get(i)) {
                primes.add(i);
            }
        }

        System.out.println("Liczb pierwszych do " + N + " jest: " + primes.size());

        System.out.println("Pierwsze 10 liczb pierwszych:");
        for (int i = 0; i < 10 && i < primes.size(); i++) {
            System.out.print(primes.get(i) + " ");
        }

        System.out.println();
        System.out.println("Koniec programu!");
    }
}