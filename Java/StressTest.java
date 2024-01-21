import Calculator.*;
import Operations.*;
import java.lang.management.ManagementFactory;
import com.sun.management.OperatingSystemMXBean;
import java.lang.management.MemoryMXBean;

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
