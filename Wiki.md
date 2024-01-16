# Code Annotations: Attributes, Decorators, and Assertions

## Overview

Welcome to the documentation for the **Code Annotations** project. This project explores various aspects of Java programming, including attributes, decorators, and assertions. The primary goal is to showcase the implementation of a simple calculator application with a menu-driven interface.

## Table of Contents

1. [Introduction](#introduction)
2. [Main method](#main-method)
3. [Calculator Abstract Class](#calculator-abstract-class)
4. [Calculator Operations](#calculator-operations)
5. [Stress Class](#stress-class)

## Introduction

The **Code Annotations** project demonstrates the use of attributes, decorators, and assertions in both Java and Python. Annotations are a form of metadata that provide information about the code to the compiler or runtime environment. Annotations can be used to add information to classes, methods, fields, and other program elements. The project includes a calculator application with a menu text-based interface, allowing users to perform various mathematical operations.

## Main Method

The `CalculatorMain` class serves as the main entry point for the program. It utilizes a menu loop to interact with users, offering options for different mathematical operations. The program supports addition, subtraction, multiplication, division, power, square root, factorial, and includes a random number stress test. SupressWarning annotation is also used to hide the deprecation error.

### Code Snippet:

```java
import java.util.Scanner;

// Class for the main program
class CalculatorMain {

    // Main method for the program
    @SuppressWarnings("deprecation") // Used to remove the deprecation warning
    public static void main(String[] args) {

        // ... (Initializations and Scanner setup)

        // Menu loop
        while (true) {
            // ... (Display menu)

            int choice = scanner.nextInt(); // Asks user for choice

            // Checks user's choice
            if (choice == 0) {
                System.out.println("Exiting the calculator.");
                break;
            }

            // Perform the chosen operation
            switch (choice) {
                // ... (Cases for different operations)
            }

            if (choice >= 1 && choice <= 5) {
                // ... (Get user input for the calculation)
                double result = operationCalc.calculate(num1, num2);
                System.out.println("Result: " + result);
            } else if (choice == 6 || choice == 7) {
                // ... (Get user input for the calculation)
                operationCalc.calculate(num);
            }

            // Deprecated method
            operationCalc.deprecatedMethod();
        }
    }
}
```
