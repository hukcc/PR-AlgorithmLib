import random
import numpy as np

class KMeans( ):
    def __init__(self):
        self.name = "k-means"
    def kMeans(self, dataArray, K):
        self.startPoints = []
        startPointIdxs = []
        distancesWithKPoints = []
        self.result = []
        lastStartPoint = []
        for i in range(K):
            startPointIdx = random.randint(0, dataArray.shape[0]-1)
            startPoint = dataArray[startPointIdx, :]
            self.startPoints.append(startPoint)
            startPointIdxs.append(startPointIdx)
            self.result.append([])
            lastStartPoint.append(np.zeros((1, np.shape(dataArray)[1]), dtype=float))
        self.cnt = 0
        while True:
            self.cnt += 1
            flag = 1
            for cnt in range(K):
                if len(self.result[cnt]) == 0:
                    flag = 0

            if flag:
                for KIdx in range(len(self.result)):
                    sumVec = np.zeros((1, np.shape(dataArray)[1]), dtype=float)
                    if len(self.result[KIdx]) > 0:
                        lastStartPoint[KIdx] = self.startPoints[KIdx]
                        for sample in self.result[KIdx]:
                            sumVec += sample
                        self.startPoints[KIdx] = sumVec/len(self.result[KIdx])
                    else:
                        newStartPointIdx = random.randint(0, dataArray.shape[0]-1)
                        newStartPoint = dataArray[startPointIdx, :]
                        self.startPoints[KIdx] = newStartPoint
                    self.result[KIdx].clear()
                        
                    

            for sampleIdx in range(np.shape(dataArray)[0]) :
                distancesWithKPoints.clear()
                for startPoint in self.startPoints:
                    
                    samplePoint = dataArray[sampleIdx, :]
                    dis = np.linalg.norm(samplePoint - startPoint)
                    distancesWithKPoints.append(dis)
                minDis = np.min(distancesWithKPoints)
                minIdx = distancesWithKPoints.index(minDis)
                self.result[minIdx].append(dataArray[sampleIdx, :])
            sumPointDis = 0
            for pointIdx in range(len(self.startPoints)):
                pointDis = np.linalg.norm(self.startPoints[pointIdx] - lastStartPoint[pointIdx])
                sumPointDis += pointDis
            
            if sumPointDis/K < 0.0001:
                break
                
        
        
        
        
        
        print("k-means done !")