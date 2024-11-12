import threading
import time
import random


n = 20


buffer = [None] * n

# Semaphores
empty_semaphore = threading.Semaphore(n)  # Semaphore to track empty slots in the buffer
full_semaphore = threading.Semaphore(0)   # Semaphore to track filled slots in the buffer
mutex_semaphore = threading.Semaphore(1)  # Mutex to ensure exclusive access to the buffer

# Index to keep track of the position in the buffer
in_index = 0
out_index = 0

def producer():
    global in_index
    for i in range(100):
        print("Producer is waiting on empty semaphore")
        empty_semaphore.acquire()
        print("Producer got access on empty semaphore")
        
        print("Producer is waiting on mutex semaphore")
        mutex_semaphore.acquire()
        print("Producer got access on mutex semaphore")

        # Critical section
        item = random.randint(1, 100)
        buffer[in_index] = item
        print(f"Producer added item with value {item} at index {in_index}")

        # Update index
        in_index = (in_index + 1) % n

        mutex_semaphore.release()
        full_semaphore.release()
        print("Producer released mutex and full semaphores")
        time.sleep(1)  # Simulating some processing time

def consumer():
    global out_index
    for i in range(100):
        print("Consumer is waiting on full semaphore")
        full_semaphore.acquire()
        print("Consumer got access on full semaphore")
        
        print("Consumer is waiting on mutex semaphore")
        mutex_semaphore.acquire()
        print("Consumer got access on mutex semaphore")

        # Critical section
        item = buffer[out_index]
        buffer[out_index] = None
        print(f"Consumer removed item with value {item} from index {out_index}")

        # Update index
        out_index = (out_index + 1) % n

        mutex_semaphore.release()
        empty_semaphore.release()
        print("Consumer released mutex and empty semaphores")
        time.sleep(2)  # Simulating some processing time

def main():
    # Create threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Start threads
    producer_thread.start()
    consumer_thread.start()

    # Join threads
    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()
