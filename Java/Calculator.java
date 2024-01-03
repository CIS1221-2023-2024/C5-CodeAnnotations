// Abstract class
abstract class Calculator {
    // Abstract method
    abstract double calculate(double num1, double num2);

    // Deprecated method
    @Deprecated
    void deprecatedMethod() {
        System.out.println("This is an example of a deprecated method.");
    }
}
