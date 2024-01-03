// Addition operation
class AddOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 + num2;
    }
}

// Subtraction operation
class SubtractOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 - num2;
    }
}

// Multiplication operation
class MultiplyOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 * num2;
    }
}

// Division operation
class DivideOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        if (num2 != 0) {
            return num1 / num2;
        }
        else {
            System.out.println("Error: Division by zero!");
            return Double.NaN; // Not a Number
        }
    }
}
