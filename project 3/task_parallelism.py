import threading   # importing a thread module that emulates Java's threading model
import math        # importing the math library 


# implementing a maximum class thread which finds the maximum value of an input list
class MaxThread(threading.Thread):
    def __init__(self, input_list):
        threading.Thread.__init__(self)
        self.input_list = input_list

    def run(self):
        max_val = max(self.input_list)
        print("Maximum value:", max_val)


# implementing a minimum class thread which finds the minimum value of an input list
class MinThread(threading.Thread):
    def __init__(self, input_list):
        threading.Thread.__init__(self)
        self.input_list = input_list

    def run(self):
        min_val = min(self.input_list)
        print("Minimum value:", min_val)

# implementing an average class thread which finds the average/mean value of an input list
class AvgThread(threading.Thread):
    def __init__(self, input_list):
        threading.Thread.__init__(self)
        self.input_list = input_list

    def run(self):
        avg_val = sum(self.input_list) / len(self.input_list)
        print("Average value:", avg_val)

# implementing a standard deviation class thread which finds the standard deviation of an input list
class StdDevThread(threading.Thread):
    def __init__(self, input_list):
        threading.Thread.__init__(self)
        self.input_list = input_list

    def run(self):
        mean = sum(self.input_list) / len(self.input_list)
        variance = sum((x - mean) ** 2 for x in self.input_list) / len(self.input_list)
        std_dev = math.sqrt(variance)
        print("Standard deviation:", std_dev)


def main():
    """
    The main function that creates threads to calculate the maximum, minimum, average, and standard deviation
    of a given list of numbers using parallelism.
    """
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Create threads for each calculation
    max_thread = MaxThread(input_list)
    min_thread = MinThread(input_list)
    avg_thread = AvgThread(input_list)
    std_dev_thread = StdDevThread(input_list)

    # Start all threads
    max_thread.start()
    min_thread.start()
    avg_thread.start()
    std_dev_thread.start()

    # Wait for all threads to finish
    max_thread.join()
    min_thread.join()
    avg_thread.join()
    std_dev_thread.join()

if __name__ == '__main__':
    main()
