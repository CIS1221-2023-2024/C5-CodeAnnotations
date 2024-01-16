class AddOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 + num2;
    }

    void calculate(long num) {

    }
}

// Subtraction operation
class SubtractOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 - num2;
    }

    void calculate(long num) {

    }
}

// Multiplication operation
class MultiplyOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 * num2;
    }

    void calculate(long num) {

    }
}

// Division operation
class DivideOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {

        assert num2 != 0 : "Divisor must not be 0."; // Checks if the divisor is 0

        if (num2 == 0){
            throw new IllegalArgumentException("Divisor must not be equal to 0.");
        }
        else{
            return num1 / num2;
        }
    }

    void calculate(long num) {

    }
}

// Power operation
class PowerOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return Math.pow(num1, num2);
    }

    void calculate(long num) {

    }
}

// Square root operation
class SquareRootOperation extends Calculator {
    @Override
    void calculate(long num) {
        assert num >= 0 : "Number needs to be greater or equal to 0.";
        System.out.println(Math.sqrt(num));
    }

    double calculate(double num1, double num2){
        return 0;
    }
}


class FactorialOperation extends Calculator {
    @Override
    void calculate(long n) {

        // Checks if number is 0 or greater
        if (n >= 0) {
            // Recursive factorial
            long startRec = System.nanoTime();
            long resultRec = calculateRec(n);
            long endRec = System.nanoTime();

            // Iterative factorial
            long startIter = System.nanoTime();
            long resultIter = calculateIter(n);
            long endIter = System.nanoTime();

            // Calculate and display execution times
            long executionRec = endRec - startRec;
            long executionIter = endIter - startIter;

            System.out.println("Recursive Factorial Result: " + resultRec);
            System.out.println("Iterative Factorial Result: " + resultIter);
            System.out.println("Execution Time (Recursive): " + executionRec + " nanoseconds");
            System.out.println("Execution Time (Iterative): " + executionIter + " nanoseconds");
        }
        else {
            assert n < 0 : "Number must be greater or equal to 0."; // Number must be greater or equal to 0
            throw new IllegalArgumentException("Number must be greater or equal to 0.");
        }
    }

    double calculate(double num1, double num2){
        return 0;
    }

    // Factorial recursively
    private long calculateRec(long n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * calculateRec(n - 1);
    }

    // Factorial iteratively
    private long calculateIter(long n) {

        long result = 1;

        for(int i = 1; i <= n; i++) {

            result *= i;
        }
        return result;
    }
}
