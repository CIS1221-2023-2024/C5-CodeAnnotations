package Operations;
import Calculator.*;
// Square root operation
public class SquareRoot extends Calculator {
    @Override
    public void calculate(long num) {

        assert num >= 0 : "Cannot calculate the square root of a negative number."; // Example of assertion

        // Checks if number is greater or equal to 0
        if (num < 0) {
            System.out.println("Cannot calculate the square root of a negative number.");
        } else {
            System.out.println(Math.sqrt(num));
        }
    }

    public double calculate(double num1, double num2) {
        return 0;
    }
}
