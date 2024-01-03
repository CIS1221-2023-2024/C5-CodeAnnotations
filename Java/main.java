import java.util.Scanner;
import java.util.Random;

// Class for the main program
class CalculatorMain {

    // Main method for executing the calculator program
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {

        // Initializing scanner
        Scanner scanner = new Scanner(System.in);

        // Menu loop
        while(true){
            // Display menu
            System.out.println("Simple Calculator Menu:");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Random Number Stress Test");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();

            // Checks user's choice
            if (choice == 0) {
                System.out.println("Exiting the calculator.");
                break;
            }

            // Perform the chosen operation
            Calculator operation;
            switch (choice) {
                case 1:
                    operation = new AddOperation();
                    break;
                case 2:
                    operation = new SubtractOperation();
                    break;
                case 3:
                    operation = new MultiplyOperation();
                    break;
                case 4:
                    operation = new DivideOperation();
                    break;
                case 5:
                    randomStressTest();
                    continue; // Skips the rest of the loop for stress test
                default:
                    System.out.println("Invalid choice. Please try again.");
                    continue; // Skips the rest of the loop if an invalid choice is given
            }

            // Get user input for the calculation
            System.out.print("Enter first number: ");
            double num1 = scanner.nextDouble();
            System.out.print("Enter second number: ");
            double num2 = scanner.nextDouble();

            // Calculate and display result
            double result = operation.calculate(num1, num2);
            System.out.println("Result: " + result);

            // Deprecated method
            operation.deprecatedMethod();
        }
    }

    // Stress test with random numbers
    private static void randomStressTest() {
        // Setting the start time for the stress test
        long startTime = System.currentTimeMillis();

        // Setting the end time for the stress test
        long endTime = startTime + 10000; // 10 seconds

        // Create an instance for the Random class
        Random random = new Random();

        // Counter for the number of calculations performed
        int calculationCount = 0;

        // Loop for the stress test
        while (System.currentTimeMillis() < endTime) {

            // Generates two random double numbers between 0 and 1000
            double num1 = random.nextDouble() * 1000;
            double num2 = random.nextDouble() * 1000;

            // Prints the generated numbers
            System.out.println("Random Number Stress Test:");
            System.out.println("Generated numbers: " + num1 + " and " + num2);

            // Create instances of Calculator for different operations
            Calculator addOperation = new AddOperation();
            Calculator subtractOperation = new SubtractOperation();
            Calculator multiplyOperation = new MultiplyOperation();
            Calculator divideOperation = new DivideOperation();

            // Prints the results
            System.out.println("Addition result: " + addOperation.calculate(num1, num2));
            System.out.println("Subtraction result: " + subtractOperation.calculate(num1, num2));
            System.out.println("Multiplication result: " + multiplyOperation.calculate(num1, num2));
            System.out.println("Division result: " + divideOperation.calculate(num1, num2));

            // Update the calculation count
            calculationCount += 4;
        }

        // Prints the total number of calculations performed during the stress test
        System.out.println("Total number of calculations: " + calculationCount);
    }
}
