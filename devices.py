class DevicesCollection:

    def __init__(self, devices_count):
        self.devices_count = devices_count
        self.device_pointer = 0
        self.devices = [(False, None)] * devices_count

    def push(self, source_time):
        start = self.device_pointer
        while True:
            if self.devices[self.device_pointer][0]:
                self.device_pointer = (1 + self.device_pointer) % self.devices_count
                if self.device_pointer == start:
                    print("no free device", start, self.device_pointer, source_time, self.devices)
                    break
            else:
                self.devices[self.device_pointer] = (True, source_time)
                return self.device_pointer

    def free_device(self, i):
        print("freeee device", i)
        self.devices[i] = (False, self.devices[i][1])

    def have_empty_device(self):
        print("have empty dev?", self.devices)
        for i in range(self.devices_count):
            if self.devices[i][0] == False:
                print("have", i)
                return True
        return False
