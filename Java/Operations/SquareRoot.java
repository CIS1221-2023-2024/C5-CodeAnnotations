package Operations;
import Calculator.*;
// Square root operation
public class SquareRoot extends Calculator {
    @Override
    public void calculate(long num) {

        assert num >= 0 : "Number needs to be greater or equal to 0."; // Checks if number is greater or equal to 0

        System.out.println(Math.sqrt(num));
    }

    public double calculate(double num1, double num2) {
        return 0;
    }
}
