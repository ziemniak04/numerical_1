import java.util.ArrayList;

/**
 * Sieve of Eratosthenes implementation for finding prime numbers.
 * 
 * This class finds all prime numbers up to a given limit N using the Sieve of Eratosthenes
 * algorithm. The limit can be provided as a command-line argument or defaults to 100,000,000.
 */
public class nm1 {
    
    /**
     * Main method to execute the prime number finding algorithm.
     * 
     * @param args Command-line arguments where args[0] is the upper limit N (optional)
     */
    public static void main(String[] args) {
        int N = 100000000;
        if (args.length > 0) {
            N = Integer.parseInt(args[0]);
        }

        boolean[] isPrime = sieveOfEratosthenes(N);
        ArrayList<Integer> primes = collectPrimes(isPrime, N);
        
        printResults(N, primes);
    }
    
    /**
     * Implements the Sieve of Eratosthenes algorithm to find prime numbers.
     * 
     * @param n The upper limit for finding prime numbers
     * @return A boolean array where isPrime[i] is true if i is prime
     */
    private static boolean[] sieveOfEratosthenes(int n) {
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            isPrime[i] = true;
        }
        
        isPrime[0] = false;
        isPrime[1] = false;
        
        int limit = (int) Math.sqrt(n);
        
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j = j + i) {
                    isPrime[j] = false;
                }
            }
        }
        
        return isPrime;
    }
    
    /**
     * Collects all prime numbers from the sieve result.
     * 
     * @param isPrime Boolean array indicating which numbers are prime
     * @param n The upper limit that was checked
     * @return ArrayList containing all prime numbers up to n
     */
    private static ArrayList<Integer> collectPrimes(boolean[] isPrime, int n) {
        ArrayList<Integer> primes = new ArrayList<>();
        
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }
        
        return primes;
    }
    
    /**
     * Prints the results including total count and first 10 prime numbers.
     * 
     * @param n The upper limit that was checked
     * @param primes ArrayList of all prime numbers found
     */
    private static void printResults(int n, ArrayList<Integer> primes) {
        System.out.println("Liczb pierwszych do " + n + " jest: " + primes.size());
        
        System.out.println("Pierwsze 10 liczb pierwszych:");
        for (int i = 0; i < 10 && i < primes.size(); i++) {
            System.out.print(primes.get(i) + " ");
        }
        System.out.println();
    }
}
