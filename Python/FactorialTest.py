import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1000000)  # Allows recursion to work on higher numbers [for factorial]
sys.set_int_max_str_digits(1000000)  # increasing the limit for converting between int and str


class FactorialGenerator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def iterative_factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def recursive_factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * FactorialGenerator.recursive_factorial(n - 1)

    @staticmethod
    def generate_numbers(self, x):
        sample_size = min(50, x + 1)  # Ensure sample size is not greater than x
        return sorted(random.sample(range(x + 1), sample_size))

    def calculate_iterative_factorials(self, numbers):
        times = []
        results = []
        total_elapsed_time = 0

        for num in numbers:
            start_time = time.time()
            result = self.iterative_factorial(num)
            end_time = time.time()
            elapsed_time = end_time - start_time
            total_elapsed_time += elapsed_time

            times.append(elapsed_time)
            results.append(result)

        self.plot_graph(numbers, times, 'Iterative Factorial Calculation Time')
        print(f"Iterative Time Total: {total_elapsed_time}")

    def calculate_recursive_factorials(self, numbers):
        times = []
        results = []
        total_elapsed_time = 0

        for num in numbers:
            start_time = time.time()
            result = self.recursive_factorial(num)
            end_time = time.time()
            elapsed_time = end_time - start_time
            total_elapsed_time += elapsed_time

            times.append(elapsed_time)
            results.append(result)

        self.plot_graph(numbers, times, 'Recursive Factorial Calculation Time')
        print(f"Recursive Time Total: {total_elapsed_time}")

    @staticmethod
    def plot_graph(x_values, y_values, title):
        plt.figure(figsize=(10, 5))
        plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
        plt.xlabel('Number')
        plt.ylabel('Time (seconds)')
        plt.title(title)
        plt.grid(True)
        plt.show()
