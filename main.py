sources_count = 3
source_delay = 1000

devices_count = 3
device_delay = 500

buffer_size = 3

modeling_time = 100000

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

import devices
devs = devices.DevicesCollection(devices_count)

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
        if devs.have_empty_device():
            print("have")
            heapq.heappush(calendar, (t + get_next_delay(device_delay), sources_count + devs.push(t)))
        elif buffer_has_place():
            push_source_time_in_buffer(t)
        else:
            reject(source_number, t)
    else:
        device_number = event[1] - sources_count
        print("device n", device_number)
        devs.free_device(device_number)
        if buffer_is_empty() == False:
            source_time = pop_source_time_from_buffer()
            heapq.heappush(calendar, (t + get_next_delay(device_delay), sources_count + devs.push(source_time)))


