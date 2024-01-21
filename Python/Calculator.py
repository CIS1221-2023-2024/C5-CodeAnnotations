from Workings import Operations


class CalculatorMain:
    def __init__(self) -> None:
        # Create an instance of the Operations class to perform calculations
        self.workings = Operations()

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
            print("9. Exit")  # Program terminates and shows the cumulative result of other previous results

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

        # Display the final result after all operations
        print(f"Result: {self.workings.result}")

    def stress_test(self):
        # Call the stress_test method from the Operations class
        self.workings.stress_test()
