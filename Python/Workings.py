import time  # Checks duration of factorial methods and stress test
import cmath  # For Square root method (Handles negative square roots as well)
import random  # For stress test number generation
import sys  # To increase recursion limit
import psutil  # To monitor system performance during stress test


sys.setrecursionlimit(1000000)  # Allows recursion to work on higher numbers [for factorial]
sys.set_int_max_str_digits(1000000)  # increasing the limit for converting between int and str


class Operations:
    def __init__(self) -> None:  # The method is not expected to return anything
        # Initialize the result attribute to store the last operation result
        self.result = 0
        # Initialize the results dictionary to track cumulative results for each operation
        self.results = {'add': 0, 'sub': 0, 'multi': 0, 'div': 0, 'power': 0, 'sqrt': 0}
        # Initialize the time attribute to store time taken for factorials
        self.elapsed_time = 0
        # Initialize the flag for recursive time print
        self.recursive_time_printed = False

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

    def IterativeFac(self, x):
        start_time = time.time()
        result = 1
        for i in range(1, x + 1):
            result *= i
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.result = result
        print(f"Iterative Result: {result}")
        print(f"Iterative Time: {elapsed_time:.20f}")

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
        print(f"Recursive Time: {elapsed_time:.20f}")

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
