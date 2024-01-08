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
            print("5. Stress Test")
            print("6. Exit")

            # Get the user's choice for the calculator operation
            choice = input("Enter operation to perform (1-6): ")

            # Validate the user's input to ensure it's a valid choice
            assert choice in ("1", "2", "3", "4", "5", "6"), "Invalid choice"

            if choice == "6":
                print("-Usage Terminated-")
                break

            # For operations other than Stress Test, get user input for two numbers
            if choice != "5":
                x = float(input("Enter the first number: "))
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
