package Operations;
import Calculator.*;
// Power operation
public class Power extends Calculator {
    @Override
    public double calculate(double num1, double num2) {
        return Math.pow(num1, num2); // Example of a standard method
    }

    public void calculate(long num) {

    }
}
