package Operations;
import Calculator.*;

// Addition operation
public class AddOperation extends Calculator {
    @Override
    public double calculate(double num1, double num2) {
        return num1 + num2;
    }
}