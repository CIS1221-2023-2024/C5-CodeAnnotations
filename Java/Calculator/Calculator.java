package Calculator;
// Abstract class
public abstract class Calculator {
    // Abstract method
    public abstract double calculate(double num1, double num2);

    // Deprecated method
    @Deprecated
    public
    void deprecatedMethod() {
        System.out.println("This is an example of a deprecated method.");
    }
}