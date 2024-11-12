class roundRobin:
    def __init__(self, time_quantum=4):
        self.queue = []
        self.time_quantum = time_quantum
        self.gantt_chart = []  # List to hold the Gantt chart entries

    def add_process(self, process_id, burst_time):
        self.queue.append({'id': process_id, 'bt': burst_time})

    def run(self):
        time = 0
        
        while not self.is_empty():
            process = self.queue.pop(0)
            
            # Simulate the running of the current process
            run_time = min(self.time_quantum, process['bt'])
            process['bt'] -= run_time
            time += run_time
            
            # Add the process to the Gantt chart with its start and end time
            if self.gantt_chart and self.gantt_chart[-1]['id'] == process['id']:
                self.gantt_chart[-1]['end'] = time
            else:
                self.gantt_chart.append({'id': process['id'], 'start': time - run_time, 'end': time})
            
            # If the process is not finished, re-enqueue it
            if process['bt'] > 0:
                self.add_process(process['id'], process['bt'])
            else:
                print(f"{process['id']} has finished executing at time {time}.")

        print("Finished processing all processes in", time, "units of time.")

    def is_empty(self):
        return len(self.queue) == 0

    def print_gantt_chart(self):
        self.process_queue = []
        print("Gantt Chart:")
        for entry in self.gantt_chart:
            self.process_queue.append(f"{entry['id']}: [{entry['start']} - {entry['end']}]")
        print(self.process_queue)

    def print_queue(self):
        for process in self.queue:
            print(f"Process ID: {process['id']}, Burst Time: {process['bt']}")

# Initialize the round robin scheduler with a time quantum
processes = roundRobin(time_quantum=4)

#Enqueue processes with their respective burst times
processes.add_process("Process 1", 8)
processes.add_process("Process 2", 6)
processes.add_process("Process 3", 3)
processes.add_process("Process 4", 2)
processes.add_process("Process 5", 4)

# Run the scheduler
processes.run()

# Print the status of the queue (should be empty after running)
processes.print_queue()

# Print the Gantt chart
processes.print_gantt_chart()
