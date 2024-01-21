from Workings import Operations


class CalculatorMain:
    def __init__(self):
        # Create an instance of the Operations class to perform calculations
        self.workings = Operations()

    def menu(self):
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
            print("9. Exit")

            # Get the user's choice for the calculator operation
            choice = input("Enter operation to perform (1-9): ")

            # Validate the user's input to ensure it's a valid choice
            assert choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"), "Invalid choice"

            if choice == "9":
                print("-Usage Terminated-")
                break

            # For operations other than Stress Test, get user input for two numbers
            if choice != "8":
                if choice == "7":
                    x_input = input("Enter the number for factorial calculation: ")

                    try:
                        x = int(x_input)
                    except ValueError:
                        raise AssertionError("Factorial input must be an integer")
                else:
                    x = float(input("Enter the first number: "))

                if choice not in ("5", "6", "7"):
                    y = float(input("Enter the second number: "))

                # Perform the selected operation based on the user's choice
                if choice == "1":
                    self.workings.add(x, y)
                elif choice == "2":
                    self.workings.sub(x, y)
                elif choice == "3":
                    self.workings.multi(x, y)
                elif choice == "4":
                    self.workings.div(x, y)
                elif choice == "5":
                    self.workings.power(x, y)
                elif choice == "6":
                    self.workings.sqrt(x)
                elif choice == "7":
                    # Calculate factorial using both recursive and iterative methods
                    recursive_result = self.workings.factorial_recursive(x)
                    iterative_result = self.workings.factorial_iterative(x)
                    # Ensure the keys are present in the results dictionary
                    self.workings.results.setdefault('factorial_recursive', 0)
                    self.workings.results.setdefault('factorial_iterative', 0)

                    # Update cumulative results
                    self.workings.results['factorial_recursive'] += recursive_result
                    self.workings.results['factorial_iterative'] += iterative_result

                    # Display the results
                    print(f"Recursive Factorial of {x}: {recursive_result}")
                    print(f"Iterative Factorial of {x}: {iterative_result}")

            elif choice == "8":
                # Perform the Stress Test and display cumulative results
                self.stress_test()
                print(f"Addition result: {self.workings.results['add']}")
                print(f"Subtraction result: {self.workings.results['sub']}")
                print(f"Multiplication result: {self.workings.results['multi']}")
                print(f"Division result: {self.workings.results['div']}")

        # Display the final result after all operations
        print(f"Result: {self.workings.result}")

    def stress_test(self):
        # Call the stress_test method from the Operations class
        self.workings.stress_test()

