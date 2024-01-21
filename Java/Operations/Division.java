package Operations;
import Calculator.*;
// Division operation
public class Division extends Calculator {
    @Override
    public double calculate(double num1, double num2) {

        assert num2 != 0 : "Divisor must not be 0."; // Example of assertion

        // Checks if the divisor is 0
        if (num2 == 0) {
            System.out.println("Divisor must not be 0, returning special value.");
            return Double.NaN;
        }
        else {
            return num1 / num2;
        }
    }

    public void calculate(long num) {

    }
}
