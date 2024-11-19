class LamportClock:
    def __init__(self):
        self.time = 0
    def increment(self):
        self.time += 1
    def send_event(self):
        self.increment()
        return self.time
    def receive_event(self, received_time):
        self.time = max(self.time, received_time) + 1
 
    def __str__(self):
        return f"Logical Clock: {self.time}"

if __name__ == "__main__":
    
    process1 = LamportClock()
    process2 = LamportClock()
    print("Process 1 performs an event.")
    
    process1.increment()
    print(process1)
    print("\nProcess 1 sends a message to Process 2.")
    
    sent_time = process1.send_event()
    print(f"Process 1 clock after sending: {process1}")
    print("\nProcess 2 receives the message from Process 1.")
    
    process2.receive_event(sent_time)
    print(f"Process 2 clock after receiving: {process2}")
    print("\nProcess 2 performs another event.")
    
    process2.increment()
    print(process2)
    print("\nProcess 2 sends a message to Process 1.")
    
    sent_time = process2.send_event()
    print(f"Process 2 clock after sending: {process2}")
    print("\nProcess 1 receives the message from Process 2.")
    
    process1.receive_event(sent_time)
    print(f"Process 1 clock after receiving: {process1}")