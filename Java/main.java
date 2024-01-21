import java.util.InputMismatchException;
import java.util.Scanner;
import Calculator.*;
import Operations.*;

// Class for the main program
class CalculatorMain {

    // Main method for the program
    @SuppressWarnings("deprecation") // Used to remove the deprecation warning
    public static void main(String[] args) {

        // Initialising
        Scanner scanner = new Scanner(System.in);
        Calculator operationCalc;
        Stress operationExtra = new Stress();

        // Menu loop
        while (true) {
            // Display menu
            System.out.println("Calculator Menu:");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Power");
            System.out.println("6. Square root");
            System.out.println("7. Factorial");
            System.out.println("8. Random Number Stress Test");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");

            int choice;

            // Error handling
            try {
                choice = scanner.nextInt(); // Asks user for choice
            }
            catch (InputMismatchException e) {
                System.out.println("Invalid choice, please try again");
                scanner.nextLine(); // Consumes the invalid input
                continue;
            }

            // Checks user's choice
            if (choice == 0) {
                System.out.println("Exiting the calculator.");
                break;
            }

            // Perform the chosen operation
            switch (choice) {
                case 1:
                    operationCalc = new Addition();
                    break;
                case 2:
                    operationCalc = new Subtraction();
                    break;
                case 3:
                    operationCalc = new Multiplication();
                    break;
                case 4:
                    operationCalc = new Division();
                    break;
                case 5:
                    operationCalc = new Power();
                    break;
                case 6:
                    operationCalc = new SquareRoot();
                    break;
                case 7:
                    operationCalc = new Factorial();
                    break;
                case 8:
                    operationExtra.randomStressTest();
                    continue; // Skips the rest of the loop
                default:
                    System.out.println("Invalid choice.");
                    continue; // Skips the rest of the loop if an invalid choice is given
            }

            try {
                if (choice >= 1 && choice <= 5) {
                    // Get user input for the calculation
                    System.out.print("Enter first number: ");
                    double num1 = scanner.nextDouble();
                    System.out.print("Enter second number: ");
                    double num2 = scanner.nextDouble();

                    // Calculate and display result
                    double result = operationCalc.calculate(num1, num2);
                    System.out.println("Result: " + result);
                }
                else if (choice == 6 || choice == 7) {
                    // Get user input for the calculation
                    System.out.print("Enter number: ");
                    long num = scanner.nextInt();

                    // Calculate and display result
                    operationCalc.calculate(num);
                }
            }
            catch (InputMismatchException e) {
                System.out.println("Invalid choice, please try again");
                scanner.nextLine(); // Consumes the invalid input
                continue;
            }

            // Deprecated method
            operationCalc.deprecatedMethod();
        }
    }
}
