sources_count = 3
source_delay = 100

devices_count = 3
device_delay = 5000

buffer_size = 3

modeling_time = 1000000

import random
import math
def get_next_delay(average):
    r = random.uniform(0, 1)
    tau = -1 * average * math.log(r)
    return tau

import heapq
calendar = []
for source_number in range(sources_count):
    heapq.heappush(calendar, (get_next_delay(source_delay), source_number))

devices = [(False, 0)] * devices_count
device_pointer = 0
def push_source_time_in_device(t):
    global device_pointer
    start = device_pointer
    while True:
        if devices[device_pointer][0]:
            device_pointer = (1 + device_pointer) % devices_count
            if device_pointer == start:
                print("no free device", start, device_pointer, t, devices)
                break
        else:
            devices[device_pointer] = (True, t)
            return device_pointer
def free_device(i):
    print("freeee device", i)
    devices[i] = (False, devices[i][1])
def have_empty_device():
    print("have empty dev", devices)
    for i in range(devices_count):
        if devices[i][0] == False:
            print("have", i)
            return True
    return False

buffer = [(False, 0)] * buffer_size
def buffer_has_place():
    for i in range(buffer_size):
        if buffer[i][0] == False:
            return True
    return False
def buffer_is_empty():
    for i in range(buffer_size):
        if buffer[i][0]:
            return False
    return True
def push_source_time_in_buffer(t):
    for i in range(buffer_size):
        if buffer[i][0] == False:
            print("push buffer n", i)
            buffer[i] = (True, t)
            break
def pop_source_time_from_buffer(): # TODO
    for i in range(buffer_size):
        if buffer[i][0]:
            print("pop buffer n", i)
            buffer[i] = (False, buffer[i][1])
            return buffer[i][1]

def reject(source_number, t):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!reject", source_number, t)

t = 0
while True:
    event = heapq.heappop(calendar)
    t += event[0]
    print("event t =", t)
    if t > modeling_time:
        print("stop")
        break
    if event[1] < sources_count:
        source_number = event[1]
        print("source n", source_number)
        heapq.heappush(calendar, (t + get_next_delay(source_delay), source_number))
        if have_empty_device():
            print("have")
            heapq.heappush(calendar, (t + get_next_delay(device_delay), sources_count + push_source_time_in_device(t)))
        elif buffer_has_place():
            push_source_time_in_buffer(t)
        else:
            reject(source_number, t)
    else:
        device_number = event[1] - sources_count
        print("device n", device_number)
        free_device(device_number)
        if buffer_is_empty() == False:
            source_time = pop_source_time_from_buffer()
            heapq.heappush(calendar, (t + get_next_delay(device_delay), sources_count + push_source_time_in_device(source_time)))


