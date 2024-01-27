# Code Annotations: Attributes, Decorators, and Assertions

## Overview

Welcome to the documentation for the **Code Annotations** project. This project explores various aspects in both Java and Python, including attributes, decorators, and assertions. The primary goal is to showcase the implementation of a calculator program that makes use of code annotations.

## Table of Contents

a. [Introduction](#introduction)


b. [Java](#introduction)
   1. [Main method](#main-method)
   2. [Abstract class](#abstract-class)
   3. [Operations file](#operations-file)
      - [Addition Class](#addition-class)
      - [Subtraction Class](#subtraction-class)
      - [Multiplication Class](#multiplication-class)
      - [Division Class](#division-class)
      - [Power Class](#power-class)
      - [SquareRoot Class](#squareroot-class)
      - [Factorial Class](#factorial-class)
   4. [Stress class](#stress-class)

      
c. [Python](#python)
   1. [Introduction](#Intro)
   2. [Main Class](#Main-Class)
   3. [Operations](#Operations)
   4. [Factorial Statistics](#Factorial-Statistics)
   5. [Runner](#Runner-Class)



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
```

```java
@SuppressWarnings("deprecation") // Used to remove the deprecation warning
```



## Abstract class

The `Calculator` class is an abstract class that serves as the foundation for implementing various mathematical operations. It contains abstract methods for performing calculations and an example of a deprecated method.

#### Code Snippet

```java
abstract public class Calculator {
    // Abstract methods and overloading
    abstract public double calculate(double num1, double num2); // Method with 2 parameters
    abstract public void calculate(long num); // Method with 1 parameter

    // An example of a deprecated method
    @Deprecated
    public void deprecatedMethod() {
        System.out.println("This is an example of a deprecated method.");
    }
}
```


## Operations package
In all classes under this package, empty methods can be found since all abstract methods needs to be overidden in each class.

### Adddition Class

The `Addition` class extends the `Calculator` abstract class and provides the implementation for addition operations.

#### Code Snippet

```java
public class Addition extends Calculator {
    @Override
    public double calculate(double num1, double num2) {
        return num1 + num2;
    }

    public void calculate(long num) {

    }
}
```

### Subtraction Class

The `Subtraction` class extends the `Calculator abstract class and provides the implementation for subtraction operations.

#### Code Snippet

```java
public class Subtraction extends Calculator {
    @Override
    public double calculate(double num1, double num2) {
        return num1 - num2;
    }

    public void calculate(long num) {

    }
}
```

### Multiplication Class

The `Multiplication` class extends the `Calculator` abstract class and provides the implementation for multiplication operations.

#### Code Snippet

```java
public class Multiplication extends Calculator {
    @Override
    public double calculate(double num1, double num2) {
        return num1 * num2;
    }

    public void calculate(long num) {

    }
}
```

### Division Class

The `Division` class extends the `Calculator` abstract class and provides the implementation for division operations. Through the use of the assert statement and if statement the variable num2 is checked to see if it is not equal to 0. If num2 is equal to 0, NaN will be returned.

#### Code Snippet

```java
public class Division extends Calculator {
    @Override
    public double calculate(double num1, double num2) {

        assert num2 != 0 : "Divisor must not be 0."; // Example of assertion

        // Checks if the divisor is 0
        if (num2 == 0) {
            System.out.println("Divisor must not be 0, returning special value.");
            return Double.NaN;
        }
        else {
            return num1 / num2;
        }
    }

    public void calculate(long num) {

    }
}
```

### Power Class

The `Power` class extends the `Calculator` abstract class and provides the implementation for power operations.

#### Code Snippet

```java
public class Power extends Calculator {
    @Override
    public double calculate(double num1, double num2) {
        return Math.pow(num1, num2); // Example of a standard method
    }

    public void calculate(long num) {

    }
}
```

### SquareRoot Class

The `SquareRoot` class extends the `Calculator` abstract class and provides the implementation for square root operations. Through the use of the assert statement and if statement the variable num2 is checked to see whether it is a negative number. If num2 is negative, "Cannot calculate the square root of a negative number" will be displayed.

#### Code Snippet

```java
package Operations;
import Calculator.*;
// Square root operation
public class SquareRoot extends Calculator {
    @Override
    public void calculate(long num) {

        assert num >= 0 : "Cannot calculate the square root of a negative number."; // Example of assertion

        // Checks if number is greater or equal to 0
        if (num < 0) {
            System.out.println("Cannot calculate the square root of a negative number.");
        } else {
            System.out.println(Math.sqrt(num));
        }
    }

    public double calculate(double num1, double num2) {
        return 0;
    }
}
```

### Factorial Class

The `Factorial` class extends the `Calculator` abstract class and provides the implementation for factorial operations. In the factorial class, a comparison is being made by running the same calculation using recursion and iteration. For each execution, the time is measured to compare which method is more efficient. Calculating the factorial iteritavely proved to be more efficient. Assertion is also used to check if the variable n is less than 0. If n is less than 0 an AssertionError and an illegal argument exception will be raised with the message "Number must be greater or equal to 0."

#### Code Snippet

```java
public class Factorial extends Calculator {
    @Override
    public void calculate(long n) {

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

    public double calculate(double num1, double num2){
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
    public void randomStressTest() {
        // Setting the start time for the stress test
        long startTime = System.currentTimeMillis();

        // Setting the end time for the stress test
        long endTime = startTime + 10000; // 10 seconds

        // Counter for the number of calculations performed
        int calculationCount = 0;

        // Counter to count total usage
        double totalCpuUsage = 0.0;
        double totalMemoryUsage = 0.0;

        // Getting the OperatingSystemMXBean and MemoryMXBean
        OperatingSystemMXBean osBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
        MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();

        System.out.println("Running stress test, please wait 10 seconds.");

        // Loop for the stress test
        while (System.currentTimeMillis() < endTime) {

            // Generates two random double numbers between 0 and 1000
            double num1 = Math.random() * 1000;
            double num2 = Math.random() * 1000;

            // Create instances of Calculator for different operations
            Calculator add = new Addition();
            Calculator sub = new Subtraction();
            Calculator mul = new Multiplication();
            Calculator div = new Division();

            // Calculate results
            add.calculate(num1, num2);
            sub.calculate(num1, num2);
            mul.calculate(num1, num2);
            div.calculate(num1, num2);

            // Update the calculation count
            calculationCount += 1;

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

### Intro

In my part of the Code Annotations project, I made a user-friendly calculator in Python. This calculator, wrapped in the `CalculatorMain` and `Operations` classes, covers essential math operations—addition, subtraction, multiplication, and more. I ensured it handles tricky situations gracefully, like preventing division by zero and offering clear messages for invalid inputs. For a real-world check, I put the calculator through a stress test, monitoring its CPU and memory usage. Additionally, I compared two methods for calculating factorials to find the most efficient approach. Essentially, my work brings a reliable and efficient Python calculator



### Main Class

The `CalculatorMain` class presents a user-friendly menu featuring standard mathematical operations and a stress test. Beyond its interface display, it incorporates a robust error-handling system that provides clear explanations to users when errors occur.

```python
    
    def menu(self) -> None:
        # Initialize x and y outside the loop to retain their values between iterations
        x = 0
        y = 0

        while True:
            print("\n--CALCULATOR--")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Power")
            print("6. Square Root")
            print("7. Factorial")
            print("8. Stress Test")
            print("9. Exit")    # Program terminates and shows the cumulative result of other previous results

```
After initializing x and y to be used for the inputs, the user is presented with all the possible functions to choose from. Regarding cumulative results, it will be tackled with the `Operations` class [here](#Operations).


### Error Handling
#### Assertions

This class has a variety of error handling systems to allow the user to understand why the input provided is flawed. The first type are assertions, which checks if the condition give evaluates to `True`. If `False`, it triggers an exception such as: "AsserionError: <ErrorMessage>"


##### Code Snippet:

```python

# Validate the user's input to ensure it's a valid choice
            assert choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"), "Invalid choice"



# Assertion for factorial input validation
                    assert x_input.isdigit(), "Factorial input must be a non-negative integer"



# Assertion for non-negative factorial input
                    assert x >= 0, "Cannot calculate factorial of a negative number"

```

The snippet above contains the assertions available in the `CalculatorMain` class which assert certain inputs must be of a certain type/range


#### Code Snippet:
```python

                    while True:
                        try:
                            x = float(input("Enter the first number: "))
                            break  # If conversion is successful, exit the loop
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")



                    while True:
                        try:
                            y = float(input("Enter the second number: "))
                            break  # If conversion is successful, exit the loop
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
```

The above handles errors related to the numbers needed to work out a calculation. If the user enters a letter or symbol instead of a number, An error pops up and the user is prompted to input the number again instead of terminating the program.



Outputting the different methods found in the `Operations`
#### Code Snippet:


```python
# Perform the selected operation based on the user's choice
                if choice == "1":
                    self.workings.add(x, y)
                elif choice == "2":
                    self.workings.sub(x, y)
                elif choice == "3":
                    self.workings.multi(x, y)
                elif choice == "4":
                    # Assertion to ensure non-zero divisor
                    assert y != 0, "Cannot divide by zero!"
                    self.workings.div(x, y)
                elif choice == "5":
                    self.workings.power(x, y)
                elif choice == "6":
                    # Can handle complex numbers i.e. √-x
                    self.workings.sqrt(x, y)
                elif choice == "7":
                    # Assertion for non-negative factorial input
                    assert x >= 0, "Cannot calculate factorial of a negative number"
                    self.workings.RecursiveFac(x)
                    self.workings.IterativeFac(x)

            elif choice == "8":
                # Perform the Stress Test and display cumulative results
                self.stress_test()
                print(f"Addition result: {self.workings.results['add']}")
                print(f"Subtraction result: {self.workings.results['sub']}")
                print(f"Multiplication result: {self.workings.results['multi']}")
                print(f"Division result: {self.workings.results['div']}")

        # Display the final result after all operations
        print(f"Result: {self.workings.result}")


```




## Operations
The `Operations` class was used to store different methods responsibile for working one of the operations available in the `CalculatorMain`: 

### Decorators []
In python, decorators are used to modify or extend the behaviours of functions or methods. They are applied using the `@decorator` syntax

#### Code Snippet: 

```python
    @log_time
    @log_operation
    def add(self, x, y):
        self.result = x + y
        self.results['add'] += self.result

    @log_time
    @log_operation
    def sub(self, x, y):
        self.result = x - y
        self.results['sub'] += self.result

    @log_time
    @log_operation
    def multi(self, x, y):
        self.result = x * y
        self.results['multi'] += self.result

    @log_time
    @log_operation
    def div(self, x, y):
        assert y != 0, "Cannot divide by zero!"
        self.result = x / y
        self.results['div'] += self.result

    @log_time
    @log_operation
    def power(self, x, y):
        self.result = x ** y
        self.results['power'] += self.result

    @log_time
    @log_operation
    def sqrt(self, x, y):
        self.result = cmath.sqrt(x)
        self.results['sqrt'] += self.result

    @log_time
    def IterativeFac(self, x):
        start_time = time.time()
        result = 1
        for i in range(1, x + 1):
            result *= i
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.result = result
        print(f"Iterative Result: {result}")
        print(f"Iterative Time: {elapsed_time:.10f}")

    @log_time
    def RecursiveFac(self, x):
        start_time = time.time()

        def recursive_helper(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * recursive_helper(n - 1)

        result = recursive_helper(x)
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.result = result
        print(f"Recursive Result: {result}")
        print(f"Recursive Time: {elapsed_time:.10f}")

```

The `@log_operation` and `@log_time` decorators are used to apply the following methods to each method found above

### Stress Test

The random stress test is designed to evaluate the performance and resource utilization of the calculator operations under simulated high-stress conditions. During a 10-second interval, the stress test generates random pairs of numbers in the range [0, 1000) and applies four fundamental arithmetic operations (Addition, Subtraction, Multiplication and Division) on these pairs. The results of each operation are accumulated, providing a cumulative summary of addition, subtraction, multiplication, and division. Additionally, the stress test reports the total number of calculations conducted within the 10-second timeframe. The test monitors and prints average CPU and memory usage, offering insights into the computational efficiency and resource consumption of the calculator operations during stress scenarios.

```python
    def stress_test(self) -> None:
        self.results = {'add': 0, 'sub': 0, 'multi': 0, 'div': 0}
        start_time = time.time()
        end_time = start_time + 10
        random_gen = random.Random()
        counter = 0

        cpu_usage = []
        memory_usage = []

        while time.time() < end_time:
            num1 = random_gen.uniform(0, 1000)
            num2 = random_gen.uniform(0, 1000)

            print("Random Number Stress Test:")
            print(f"Generated numbers: {num1} and {num2}")

            self.add(x=num1, y=num2)
            self.sub(x=num1, y=num2)
            self.multi(x=num1, y=num2)
            self.div(x=num1, y=num2)

            counter += 4

            # Capture CPU and memory usage
            cpu_usage.append(psutil.cpu_percent())
            memory_usage.append(psutil.virtual_memory().percent)

        print(f"Total number of calculations: {counter}")
        real_end_time = time.time()
        elapsed_time = real_end_time - start_time
        print(f"Elapsed time: {elapsed_time:.4f} seconds")

        # Calculate and display average CPU and memory usage
        avg_cpu = sum(cpu_usage) / len(cpu_usage)
        avg_memory = sum(memory_usage) / len(memory_usage)

        print(f"Average CPU Usage: {avg_cpu}%")
        print(f"Average Memory Usage: {avg_memory}%")
```


#### Code Snippet:
```python
@staticmethod
    def log_operation(func):
        def wrapper(self, x, y):
            result = func(self, x, y)
            if func.__name__ != 'sqrt':
                print(f"{func.__name__}: {x} and {y} = {self.result}")
            else:
                print(f"{func.__name__}: {x} = {self.result}")
            return result
        return wrapper

    @staticmethod
    def log_time(func):
        def wrapper(self, *args, **kwargs):
            start_time = time.time()
            result = func(self, *args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Time taken: {elapsed_time: .20f}")
            return result  # Return the result

        return wrapper
```


`log_operation` is used to print the results of every function that calls it via the `@log_operation`

`log_time` is used to measure the execution time for every operation, with a focus on comparing the performance of recursive and iterative factorial methods. It specifically aims to assess the efficiency of these methods when dealing with exceptionally large numbers, up to the factorial of 205,000.


With the `@log_time` and `@log_operation` decorator being applied to each method, besides the mathematical operation being worked out, it also activates the methods `log_time` `log_operation`.


## Recursive and Iterative Factorial Calculation

```python
@log_time
    def IterativeFac(self, x):
        start_time = time.time()
        result = 1
        for i in range(1, x + 1):
            result *= i
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.result = result
        print(f"Iterative Result: {result}")
        print(f"Iterative Time: {elapsed_time:.10f}")

    @log_time
    def RecursiveFac(self, x):
        start_time = time.time()

        def recursive_helper(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * recursive_helper(n - 1)

        result = recursive_helper(x)
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.result = result
        print(f"Recursive Result: {result}")
        print(f"Recursive Time: {elapsed_time:.10f}")

```

## Factorial Statistics

This class was created to help visualize the amount taken between different numbers, large and small. The user can set the range of numbers to be taken 1 - 205,000 and the program chooses 50 random numbers within the range and performs the factorial using both the iterative and recursive approach. Once done, a graph displaying the number generated and the time taken is generated for both methods. The program also outputs the total time taken for each method.

### Code Snippet:

```python
@staticmethod
    def plot_graph(x_values, y_values, title):
        plt.figure(figsize=(10, 5))
        plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
        plt.xlabel('Number')
        plt.ylabel('Time (seconds)')
        plt.title(title)
        plt.grid(True)
        plt.show()
```
This code snippet defines a method to be used from both the iterative and recursive methods to plot the graph. This was done using MatPlotLib. 

A test was carried out using 50 numbers from the range 0 - 150,000. These were the results on an
Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz   1.19 GHz

### Iterative Method
Graph: 
<img width="670" alt="Screenshot 2024-01-27 163031" src="https://github.com/CIS1221-2023-2024/C5-CodeAnnotations/assets/150332534/1a49ddd3-160a-4fd0-8efa-ee19f0274759">

Total time taken: 253.45079231262207

### Recursive Method
Graph: 
<img width="663" alt="Screenshot 2024-01-27 163827" src="https://github.com/CIS1221-2023-2024/C5-CodeAnnotations/assets/150332534/78fc5a0a-80d7-487e-9c13-0e5e9616f4a1">

Total time taken: 191.62772417068481



## Runner

### This class is used as a runner, it takes in the CalculatorMain and executes.
#### Code Snippet:

```python
# This is the runner class
from Calculator import CalculatorMain

calculator_test = CalculatorMain()

calculator_test.menu()
```
