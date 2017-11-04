'''create classes modeling a call center; python3'''
from datetime import datetime

class Call():
    def __init__(self, id, caller_name, caller_phone, time, purpose):
        self.id = id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time = time
        self.purpose = purpose
        
    def display(self):
        print("unique id: " + str(self.id))
        print("Name of Caller: " + str(self.caller_name))
        print("Phone Number: " + str(self.caller_phone))
        print("Time: " + str(self.time))
        print("Purpose of call: " + str(self.purpose))
        
class CallCenter():
    def __init__(self):
        self.calls = []
        self.queue_size = 0
        
    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self
        
    def remove(self, call):
        self.calls.pop(0)
        self.queue_size -= 1
        return self
        
    def remove_by_phone(self, number):
        for call in self.calls:
            if call.caller_phone is number:
                self.calls.remove(call)
            self.queue_size = len(self.calls)
        return self
        
    def info (self):
        for call in self.calls:
            print("Name: " + call.caller_name + " Phone: " + call.caller_phone)
        print ("Calls waiting: " + str(self.queue_size))
        return self 
        
    def sort_by_time(self):
        self.calls = sorted(self.calls, key=lambda call: call.time, reverse=True)
        


call1=Call(1, 'lisa', "222-333-3333", datetime.now(), "complain")
call2=Call(2, 'bob', "222-555-5555",  datetime.now(), "return")
call3=Call(1, 'kim', "222-888-8888", datetime.now(), "order")
call3.display()

monday = CallCenter()
monday.add(call1).add(call2).add(call3)
monday.sort_by_time()
monday.info()

monday.remove(call2)
monday.info()
monday.remove_by_phone('222-888-8888')
monday.info()
