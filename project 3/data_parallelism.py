import threading # importing a thread module that emulates Java's threading model
import statistics # importing the statistics library 

# a singular function to calculate the min, max, average and standard deviation of a sublist of values from a larger input list.
def calculate_statistics(sub_input_list):
    minimum = min(sub_input_list)
    maximum = max(sub_input_list)
    average = statistics.mean(sub_input_list)
    standard_deviation = statistics.stdev(sub_input_list)
    print(f"Minimum: {minimum}, Maximum: {maximum}, Average: {average}, Standard Deviation: {standard_deviation}")

# a function that separates the input lists into sublists based on the number of threads(4).
def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    num_threads = 4
    sub_input_lists = [input_list[i:i+len(input_list)//num_threads] for i in range(0, len(input_list), len(input_list)//num_threads)]
    threads = []
    for sub_input_list in sub_input_lists:
        thread = threading.Thread(target=calculate_statistics, args=(sub_input_list,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
