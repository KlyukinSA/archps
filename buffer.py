class BufferCollection:

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = [(False, None)] * buffer_size

    def has_place(self):
        for i in range(self.buffer_size):
            if self.buffer[i][0] == False:
                return True
        return False

    def is_empty(self):
        for i in range(self.buffer_size):
            if self.buffer[i][0]:
                return False
        return True

    def push(self, source_time):
        for i in range(self.buffer_size):
            if self.buffer[i][0] == False:
                print("push buffer n", i)
                self.buffer[i] = (True, source_time)
                break

    def pop_source_time(self): # TODO
        for i in range(self.buffer_size):
            if self.buffer[i][0]:
                print("pop buffer n", i)
                self.buffer[i] = (False, self.buffer[i][1])
                return self.buffer[i][1]
