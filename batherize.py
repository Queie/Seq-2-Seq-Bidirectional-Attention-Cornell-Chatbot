import numpy as np
class batherize:
    def __init__(self, train_x, train_y, batch_size=10):
        self.i = 0
        self.train_x = train_x
        self.train_y = train_y
        assert len(self.train_x) == len(self.train_y)
        self.n = len(train_x)
        self.b = self.n / batch_size
        self.batch_size = batch_size

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += self.batch_size
            return self.train_x[i:self.i], self.train_y[i:self.i]
        else:
            raise StopIteration()
