import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Fibonacci {

    // Returns the first n Fibonacci numbers: 0, 1, 1, 2, 3, 5, ...
    // BigInteger is required because F(93) and above overflow a 64-bit long.
    public static List<BigInteger> firstFibonacci(int n) {
        List<BigInteger> result = new ArrayList<>(n);
        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        for (int i = 0; i < n; i++) {
            result.add(a);
            BigInteger next = a.add(b);
            a = b;
            b = next;
        }
        return result;
    }

    public static void main(String[] args) {
        List<BigInteger> fib = firstFibonacci(100);
        for (int i = 0; i < fib.size(); i++) {
            System.out.println((i + 1) + ": " + fib.get(i));
        }
    }
}