package Operations;
import Calculator.*;

// Division operation
public class DivideOperation extends Calculator {
    @Override
    public double calculate(double num1, double num2) {
        if (num2 != 0) {
            return num1 / num2;
        }
        else {
            System.out.println("Error: Division by zero!");
            return Double.NaN; // Not a Number
        }
    }
}