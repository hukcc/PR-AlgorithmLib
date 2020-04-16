import random

class datadevider():
    def __init__(self):
        pass

    def K_devide(self, labels, dataspace):
        # data devide K = 10  ......
        self.k_batch = [ [], [], [], [], [], [], [], [], [], [] ]
        for kind in dataspace:
            i = 0
            for sample in kind:
                self.k_batch[(i % 10)].append(sample)
                i += 1

    def get_valid_and_train(self):
        self.valid_idx = random.randrange(9)
        self.train_data = []
        self.valid_data = []

        for batch in self.k_batch:
            if self.k_batch.index(batch) == self.valid_idx:
                self.valid_data = batch
            else:
                self.train_data += batch

