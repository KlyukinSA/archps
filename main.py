sources_count = 3
source_delay = 1000

devices_count = 2
device_delay = 5000

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

import buffer
buf = buffer.BufferCollection(buffer_size)

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
        elif buf.has_place():
            buf.push(t)
        else:
            reject(source_number, t)
    else:
        device_number = event[1] - sources_count
        print("device n", device_number)
        devs.free_device(device_number)
        if buf.is_empty() == False:
            source_time = buf.pop_source_time()
            heapq.heappush(calendar, (t + get_next_delay(device_delay), sources_count + devs.push(source_time)))


