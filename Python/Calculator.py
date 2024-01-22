from Workings import Operations
from FactorialTest import FactorialGenerator


class CalculatorMain:
    def __init__(self) -> None:
        # Create an instance of the Operations class to perform calculations
        self.workings = Operations()
        self.factorial_generator = FactorialGenerator()

    def menu(self) -> None:
        # Initialize x and y outside the loop to retain their values between iterations
        x = 0
        y = 0

        def perform_factorial_operations(self):
            numbers = self.factorial_generator.generate_numbers(self)
            self.factorial_generator.calculate_iterative_factorials(numbers)
            self.factorial_generator.calculate_recursive_factorials(numbers)

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
            print("9. Factorial Recursive vs Iterative Test")
            print("10. Exit")    # Program terminates and shows the cumulative result of other previous results

            # Get the user's choice for the calculator operation
            choice = input("Enter operation to perform (1-10): ")

            # Validate the user's input to ensure it's a valid choice
            assert choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), "Invalid choice"

            if choice == "10":
                print("-Usage Terminated-")
                break

            # For operations other than Stress Test, get user input for two numbers
            if choice != "8" and choice != "9":
                if choice == "7":
                    x_input = input("Enter the number for factorial calculation: ")

                    # Assertion for factorial input validation
                    assert x_input.isdigit(), "Factorial input must be a non-negative integer"
                    x = int(x_input)
                else:
                    while True:
                        try:
                            x = float(input("Enter the first number: "))
                            break  # If conversion is successful, exit the loop
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")

                if choice not in ("6", "7"):
                    while True:
                        try:
                            y = float(input("Enter the second number: "))
                            break  # If conversion is successful, exit the loop
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")

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

            elif choice == "9":
                print("Set the range of numbers you want to perform factorials on")
                print("Example, x = 50000 will generate 50 numbers in the range 0 - 50000")
                print("Factorials will be done on all these numbers in an iterative and recursive way")
                print("2 graphs will show the time taken against each number generated")
                print("For a better spread I suggest you write between 50,000 - 205000 (max)")
                print("Note: Anything > 150,000 may take a few minutes")
                while True:
                    x_input = input("Enter a positive integer x: ")

                    # Check if x is a positive integer
                    if x_input.isdigit() and int(x_input) > 0:
                        x = int(x_input)
                        break
                    else:
                        print("Invalid input. Please enter a valid positive integer.")

                print("Calculating and Plotting...")
                # Generate numbers
                numbers = self.factorial_generator.generate_numbers(self, x)

                # Perform factorial operations
                self.factorial_generator.calculate_iterative_factorials(numbers)
                self.factorial_generator.calculate_recursive_factorials(numbers)

        # Display the final result after all operations
        print(f"Result: {self.workings.result}")

    def stress_test(self):
        # Call the stress_test method from the Operations class
        self.workings.stress_test()
