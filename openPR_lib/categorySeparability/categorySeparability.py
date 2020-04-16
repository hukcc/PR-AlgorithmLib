import math
import numpy as np

class categorySeperability():
    def __init__(self):
        pass
    def distanceBasedJudge(self, features, labels, totalSampleNumber):    #   偷个懒 直接使用类别之间样本的距离均值作为判据
        J = 0
        for i in range(len(features)):
            for j in range(i+1,len(features)):
                class1Features = features[i]
                class2Features = features[j]
                disSum = 0
                for sample1  in class1Features:
                    for sample2 in class2Features:
                        disSum += np.linalg.norm(sample1-sample2)
                Jij = (disSum/(len(class1Features) * len(class2Features)))*(len(class1Features)/totalSampleNumber)*(len(class2Features)/totalSampleNumber)*0.5
                J+=Jij
        return J

    def probabilityBasedJudge(self, features, labels, totalSampleNumber, funcName):
        if funcName == "Bhattacharyya":
            pass
        elif funcName == "Chernoff":
            pass
        elif funcName == "Div":
            pass

    def entropyBasedJudge(self, features, labels):
        pass