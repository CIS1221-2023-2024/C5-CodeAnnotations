// Abstract class
abstract class Calculator {
    // Abstract methods and overloading
    abstract double calculate(double num1, double num2); // Method with 2 parameters
    abstract void calculate(long num); // Method with 1 parameter

    // An example of a deprecated method
    @Deprecated
    void deprecatedMethod() {
        System.out.println("This is an example of a deprecated method.");
    }
}
