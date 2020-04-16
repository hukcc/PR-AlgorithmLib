import numpy as np

class fisher():
    def __init__(self, labels, train):
        self.name = "Fisher"
        self.labels = labels
        self.train = train
        self.final_m = []
        self.final_s = []
        self.sw = np.zeros(shape=(len(self.train[0])-1, len(self.train[0])-1) )
        self.final_w_star_T = []
        self.reduction_vaild_result = []
        self.reduction_train_result = []


    def get_m(self):
        m = []     # 确保labels和m对应
        cnt = []
        for label in self.labels:
            temp_m = np.zeros(len(self.train[0])-1 )
            m.append(temp_m)
            cnt.append(0)

        for crr_sample in self.train:
            sample_label = crr_sample[-1]
            sample_feature = np.array(crr_sample[0:len(crr_sample)-1], dtype=float)

            for label in self.labels:
                if sample_label == label:
                    m[self.labels.index(label)] += sample_feature
                    cnt[self.labels.index(label)] += 1
        count = 0
        for mm in m:
            mm = mm / cnt[count]
            self.final_m.append(mm)
            count += 1
            
    def get_s(self):
        s = []
        for label in self.labels:
            temp_s = np.zeros(shape=(len(self.train[0])-1, len(self.train[0])-1) )
            s.append(temp_s)
        for crr_sample in self.train:
            sample_label = crr_sample[-1]
            sample_feature = np.array(crr_sample[0:len(crr_sample)-1], dtype=float)

            for label in self.labels:
                if sample_label == label:
                    ss =  np.dot(np.array([sample_feature - self.final_m[self.labels.index(label)]]).T, ([sample_feature - self.final_m[self.labels.index(label)]]) )
                    s[self.labels.index(label)] += ss
        self.final_s = s
    
    def get_sw(self):
        for s in self.final_s:
            self.sw += s

    def get_w_star_T(self):
        w_star_T = []       # for exp we have 3 class so w_star_T = [w_star_T12, w_star_T23, w_star_T31] ps:对应标签顺序
        for label in self.labels:
            temp_w_star_T = np.array(np.dot(np.linalg.inv(self.sw) , np.array([self.final_m[self.labels.index(label)] - self.final_m[(self.labels.index(label)+1)%len(self.labels)]]).T)).T
            w_star_T.append(temp_w_star_T)
        self.final_w_star_T = w_star_T
        

    def reduction(self, vaild_data, train_data):
        self.get_m()
        self.get_s()
        self.get_sw()
        self.get_w_star_T()
        
        reduction_vaild_result = []
        for w_star_T in self.final_w_star_T:
            temp_reduction_vaild_result = []
            reduction_vaild_result.append(temp_reduction_vaild_result)
        for crr_sample in vaild_data:
            sample_label = crr_sample[-1]
            sample_feature = np.array(crr_sample[0:len(crr_sample)-1], dtype=float)

            count = 0
            for w_star_T in self.final_w_star_T:
                w = np.dot(w_star_T, np.array([sample_feature]).T)
                temp_w = [w[0][0], sample_label]
                reduction_vaild_result[count % len(self.final_w_star_T)].append(temp_w)
                count += 1
        self.reduction_vaild_result = reduction_vaild_result

        reduction_train_result = []
        for w_star_T in self.final_w_star_T:
            temp_reduction_train_result = []
            reduction_train_result.append(temp_reduction_train_result)
        for crr_sample in train_data:
            sample_label = crr_sample[-1]
            sample_feature = np.array(crr_sample[0:len(crr_sample)-1], dtype=float)

            count = 0
            for w_star_T in self.final_w_star_T:
                w = np.dot(w_star_T, np.array([sample_feature]).T)
                temp_w = [w[0][0], sample_label]
                reduction_train_result[count % len(self.final_w_star_T)].append(temp_w)
                count += 1
        self.reduction_train_result = reduction_train_result

    def classification():
        pass

    


    
        