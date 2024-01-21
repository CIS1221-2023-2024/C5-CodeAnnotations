package Operations;
import Calculator.*;
// Division operation
public class Division extends Calculator {
    @Override
    public double calculate(double num1, double num2) {

        assert num2 != 0 : "Divisor must not be 0."; // Example of assertion

        // Checks if the divisor is 0
        if (num2 == 0) {
            throw new IllegalArgumentException("Divisor must not be 0.");
        }
        else {
            return num1 / num2;
        }
    }

    public void calculate(long num) {

    }
}
