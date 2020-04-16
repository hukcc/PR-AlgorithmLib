import numpy as np
from queue import Queue

class K_Nearest_Neighbor():
    def __init__ (self, K = 5):
        self.name = "K_Nearest_Neighbor"
        self.K = K
        # self.queue = Queue(K)
        self.result_list = []
        self.vaild_data_result = []
    def KNN(self, train, valid, labels):
        
        for vaild_sample in valid:       #    valid[0]      this part need to be improved 关于投影方向上的一些东西
            vaild_sample_label = vaild_sample[-1]
            vaild_sample_feature = np.array(vaild_sample[0:len(vaild_sample)-1], dtype=float)
            self.result_list.clear()
            cnt_space = []
            for label in labels:
                cnt_space.append(0)
            for train_sample in train:      #   train[0]
                train_sample_label = train_sample[-1]
                train_sample_feature = np.array(train_sample[0:len(train_sample)-1], dtype=float)
                
                dis = np.linalg.norm((vaild_sample_feature-train_sample_feature))
                self.result_list.append([dis, train_sample_label])

            self.result_list.sort(key=lambda result: result[0])
            
            for cnt in range(self.K):
                for label in labels:
                    if label == self.result_list[cnt][1]:
                        cnt_space[labels.index(label)] += 1
            max_cnt = 0
            for cnt in cnt_space:
                if cnt > max_cnt:
                    max_cnt = cnt
            self.vaild_data_result.append([vaild_sample[0:len(vaild_sample)-1], labels[cnt_space.index(max_cnt)]])
                




