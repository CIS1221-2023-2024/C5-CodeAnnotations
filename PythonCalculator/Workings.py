import time
import random

class Operations:
    def __init__(self):
        # Initialize the result attribute to store the last operation result
        self.result = 0
        # Initialize the results dictionary to track cumulative results for each operation
        self.results = {'add': 0, 'sub': 0, 'multi': 0, 'div': 0}

    @staticmethod
    def log_operation(func):
        """
        A decorator to log the operation, input values, and result.

        :param func: The operation function to be decorated.
        :return: The decorated function.
        """
        def wrapper(self, x, y):
            # Call the original operation function
            result = func(self, x, y)
            # Print the operation details
            print(f"{func.__name__}: {x} and {y} = {self.result}")
            return result
        return wrapper

    @log_operation
    def add(self, x, y):
        # Perform addition operation and update the result and cumulative result
        self.result = x + y
        self.results['add'] += self.result

    @log_operation
    def sub(self, x, y):
        # Perform subtraction operation and update the result and cumulative result
        self.result = x - y
        self.results['sub'] += self.result

    @log_operation
    def multi(self, x, y):
        # Perform multiplication operation and update the result and cumulative result
        self.result = x * y
        self.results['multi'] += self.result

    @log_operation
    def div(self, x, y):
        # Perform division operation, update the result and cumulative result
        assert y != 0, "Cannot divide by zero!"  # Assertion: Ensure y is not zero
        self.result = x / y
        self.results['div'] += self.result

    def stress_test(self):
        # Reset results before stress test
        self.results = {'add': 0, 'sub': 0, 'multi': 0, 'div': 0}

        # Setting the start time
        start_time = time.time()

        # Setting the end time for 10 seconds
        end_time = start_time + 10

        # Create an instance for the Random class
        random_gen = random.Random()

        # Counter for the number of calculations performed
        counter = 0

        # Loop for the stress test
        while time.time() < end_time:
            # Generate two random numbers
            num1 = random_gen.uniform(0, 1000)
            num2 = random_gen.uniform(0, 1000)

            print("Random Number Stress Test:")
            print(f"Generated numbers: {num1} and {num2}")

            # Use the calculator instance to perform calculations
            self.add(x=num1, y=num2)
            self.sub(x=num1, y=num2)
            self.multi(x=num1, y=num2)
            self.div(x=num1, y=num2)

            # Increment the counter
            counter += 4

        # Print the total number of calculations and elapsed time
        print(f"Total number of calculations: {counter}")
        real_end_time = time.time()
        elapsed_time = real_end_time - start_time
        print(f"Elapsed time: {elapsed_time:.4f} seconds")
