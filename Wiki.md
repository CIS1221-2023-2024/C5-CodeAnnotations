# Code Annotations: Attributes, Decorators, and Assertions

## Overview

Welcome to the documentation for the **Code Annotations** project. This project explores various aspects in both Java and Python, including attributes, decorators, and assertions. The primary goal is to showcase the implementation of a calculator program that makes use of code annotations.

## Table of Contents

a. [Introduction](#introduction)


b. [Java](#introduction)
   1. [Main method](#main-method)
   2. [Abstract class](#abstract-class)
   3. [Operations file](#operations-file)
      - [AddOperation Class](#operation-class)
      - [SubtractOperation Class](#addoperation-class)
      - [MultiplyOperation Class](#subtractoperation-class)
      - [DivideOperation Class](#divideoperation-class)
      - [PowerOperation Class](#poweroperation-class)
      - [SquareRootOperation Class](#squarerootoperation-class)
      - [FactorialOperation Class](#factorialoperation-class)
   4. [Stress class](#stress-class)

      
c. [Python](#python)



## Introduction

The **Code Annotations** project demonstrates the use of attributes, decorators, and assertions in both Java and Python. Annotations are a form of metadata that provide information about the code to the compiler or runtime environment. Annotations can be used to add information to classes, methods, fields, and other program elements. The project includes a calculator application with a menu text-based interface, allowing users to perform various mathematical operations.



# Java


## Main Method

The `CalculatorMain` class serves as the main entry point for the program. It utilizes a menu loop to interact with users, offering options for different mathematical operations. The program supports addition, subtraction, multiplication, division, power, square root, factorial, and includes a random number stress test. In addition, it handles input mismatch errors. SupressWarning annotation is also used to hide the deprecation error.

#### Code Snippet

```java
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
...
```

```java
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
```

```java
// Deprecated method
operationCalc.deprecatedMethod();
```



## Abstract class

The `Calculator` class is an abstract class that serves as the foundation for implementing various mathematical operations. It contains abstract methods for performing calculations and an example of a deprecated method.

#### Code Snippet

```java
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
```


## Operations file
In all classes under this file, empty methods can be found since all abstract methods needs to be overidden in each class.

### AddOperation Class

The `AddOperation` class extends the `Calculator` abstract class and provides the implementation for addition operations.

#### Code Snippet

```java
// Addition operation
class AddOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 + num2;
    }

    void calculate(long num) {
        // This method intentionally left blank for single-parameter calculation
    }
}
```

### SubtractOperation Class

The SubtractOperation class extends the Calculator abstract class and provides the implementation for subtraction operations.

#### Code Snippet

```java
// Subtraction operation
class SubtractOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 - num2;
    }

    void calculate(long num) {
        // This method intentionally left blank for single-parameter calculation
    }
}
```

### MultiplyOperation Class

The MultiplyOperation class extends the Calculator abstract class and provides the implementation for multiplication operations.

#### Code Snippet

```java
// Multiplication operation
class MultiplyOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return num1 * num2;
    }

    void calculate(long num) {
        // This method intentionally left blank for single-parameter calculation
    }
}
```

### DivideOperation Class

The `DivideOperation` class extends the `Calculator` abstract class and provides the implementation for division operations. Through the use of the assert statement the variable num2 is checked to see if it is not equal to 0. If num2 is equal to 0, the assertion will raise an AssertionError with the message "Divisor must not be 0."

#### Code Snippet

```java
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
        // This method intentionally left blank for single-parameter calculation
    }
}
```

### PowerOperation Class

The `PowerOperation` class extends the `Calculator` abstract class and provides the implementation for power operations.

#### Code Snippet

```java
// Power operation
class PowerOperation extends Calculator {
    @Override
    double calculate(double num1, double num2) {
        return Math.pow(num1, num2);
    }

    void calculate(long num) {
        // This method intentionally left blank for single-parameter calculation
    }
}
```

### SquareRootOperation Class

The `SquareRootOperation` class extends the `Calculator` abstract class and provides the implementation for square root operations. Through the use of the assert statement the variable num2 is checked to see if it is greater or equal to 0. If num2 is not greater or equal to 0, the assertion will raise an AssertionError with the message "Number needs to be greater than or equal to 0."

#### Code Snippet

```java
// Square root operation
class SquareRootOperation extends Calculator {
    @Override
    void calculate(long num) {
        assert num >= 0 : "Number needs to be greater or equal to 0.";
        System.out.println(Math.sqrt(num));
    }

    double calculate(double num1, double num2){
        // This method intentionally left blank for double-parameter calculation
        return 0;
    }
}
```

### FactorialOperation Class

The `FactorialOperation` class extends the `Calculator` abstract class and provides the implementation for factorial operations. In the factorial class, a comparison is being made by running the same calculation using recursion and iteration. For each execution, the time is measured to compare which method is more efficient. Assertion is also used to check if the variable n is less than 0. If n is less than 0 an AssertionError will be raised with the message "Number must be greater or equal to 0."

#### Code Snippet

```java
// Factorial operation
class FactorialOperation extends Calculator {
    @Override
    void calculate(long n) {

        // Checks if the number is 0 or greater
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
        } else {
            assert n < 0 : "Number must be greater or equal to 0.";
            // Number must be greater or equal to 0
            throw new IllegalArgumentException("Number must be greater or equal to 0.");
        }
    }

    double calculate(double num1, double num2){
        // This method intentionally left blank for double-parameter calculation
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
```



## Stress class

The `Stress` class contains a method for performing a random stress test on mathematical operations, measuring CPU and memory usage. The four standard operations were applied to the two numbers generated. Through the use of Java library, the CPU and memory usage were calculated.

#### Code Snippet

```java
class Stress {
    void randomStressTest() {
        // Setting the start time for the stress test
        long startTime = System.currentTimeMillis();

        // Setting the end time for the stress test
        long endTime = startTime + 10000; // 10 seconds

        // Counter for the number of calculations performed
        int calculationCount = 0;

        // Counter to count total usage
        double totalCpuUsage = 0.0;
        double totalMemoryUsage = 0.0;

        // Get the OperatingSystemMXBean and MemoryMXBean
        OperatingSystemMXBean osBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
        MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();

        System.out.println("Running stress test, please wait 10 seconds.");

        // Loop for the stress test
        while (System.currentTimeMillis() < endTime) {

            // Generates two random double numbers between 0 and 1000
            double num1 = Math.random() * 1000;
            double num2 = Math.random() * 1000;

            // Create instances of Calculator for different operations
            Calculator AddOperation = new AddOperation();
            Calculator SubtractOperation = new SubtractOperation();
            Calculator MultiplyOperation = new MultiplyOperation();
            Calculator DivideOperation = new DivideOperation();

            // Calculate results
            AddOperation.calculate(num1, num2);
            SubtractOperation.calculate(num1, num2);
            MultiplyOperation.calculate(num1, num2);
            DivideOperation.calculate(num1, num2);

            // Update the calculation count
            calculationCount += 4;

            // Addition of the CPU and memory usage
            totalCpuUsage += osBean.getSystemCpuLoad() * 100;
            totalMemoryUsage += memoryBean.getHeapMemoryUsage().getUsed() / (1024 * 1024);
        }

        // Calculate and print the average CPU and memory usage
        double averageCpuUsage = totalCpuUsage / calculationCount;
        double averageMemoryUsage = totalMemoryUsage / calculationCount;

        System.out.println("Average CPU Usage: " + averageCpuUsage + "%");
        System.out.println("Average Memory Usage: " + averageMemoryUsage + " MB");
        System.out.println("Total number of calculations: " + calculationCount);
    }
}
```



# Python
