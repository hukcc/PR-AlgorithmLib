import os
import numpy as np

def file_name(file_dir):   
        L=[]   
        for root, dirs, files in os.walk(file_dir):  
            for file in files:      
                L.append(os.path.join(root, file))  
        return L  


class dataloader( ):
    def __init__(self, data_path):
        self.data_paths_ = data_path      # self.data_paths_ is a list of file path
        if len(self.data_paths_) == 0:
            print("there is no data file in data dir")
        else:
            print("we have a data file" )
        
        

    def load_data(self):
        self. labels = []
        self.data_space = []
        crr_file = open(self.data_paths_)
        lines = crr_file.readlines()
        self.sampleNumber = len(lines)
        for line in lines:
            line = line.rstrip("\n")
            elements = line.split(',')      # maybe need to add same other smybal i will add it since i meet that situation
            sample_label = elements[-1]
            self.featureLenth = len(elements)-1
            label_exists = False
            for exists_label in self.labels:
                if exists_label == sample_label:
                    label_exists = True
            if label_exists == True:
                self.data_space[self.labels.index(sample_label)].append(elements)
            else:
                self.labels.append(sample_label)
                self.data_space.append([])
                self.data_space[self.labels.index(sample_label)].append(elements)
        crr_file.close()


    def load_USPS(self):
        self. labels = []
        self.data_space = []
        crr_file = open(self.data_paths_)
        lines = crr_file.readlines()
        
        for line in lines:
            line = line.rstrip("\n")
            elements = line.split(' ')      # maybe need to add same other smybal i will add it since i meet that situation
            sample_label = elements[0]
            label_exists = False
            for exists_label in self.labels:
                if exists_label == sample_label:
                    label_exists = True
            if label_exists == True:
                features = []
                for i in range(1,257):
                    feature = elements[i].split(':')[-1]
                    features.append(feature)
                features.append(sample_label)
                self.data_space[self.labels.index(sample_label)].append(features)
            else:
                self.labels.append(sample_label)
                self.data_space.append([])
                features = []
                for i in range(1,257):
                    feature = elements[i].split(':')[-1]
                    features.append(feature)
                features.append(sample_label)
                self.data_space[self.labels.index(sample_label)].append(features)
        crr_file.close()


    def loadDataAsArray(self):
        self. labels = []   #   每一个label对应dataspace中的一行
        self.data_space = []
        crr_file = open(self.data_paths_)
        lines = crr_file.readlines()
        
        for line in lines:
            line = line.rstrip("\n")
            elements = line.split(',')      # maybe need to add same other smybal i will add it since i meet that situation
            sample_label = elements.pop()
            self.featureLenth = len(elements)
           
            self.labels.append(sample_label)
            self.data_space.append(elements)
        crr_file.close()
        self.dataArray = np.array(self.data_space, dtype=float)
            
    def changeData2Array(self):
        self.dataSpaceArray = []
        for category in self.data_space:
            for sample in category:
                 sample.pop()
            arr = np.array(category, dtype=float)
            self.dataSpaceArray.append(arr)

