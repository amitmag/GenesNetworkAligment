import pandas as pd
from Gene import Gene
from scipy.stats.stats import pearsonr
import csv
path = "C:\\Users\\USER\\Documents\\work\\"


def findImportantGenes( numOfCells, *calls):
    firstStage = list()
    array = calls[0].as_matrix()
    for row in array:
        gene = Gene(row)
        if gene.numOfExpressedCells / numOfCells >= 0:
            firstStage.append(gene)
    numToChoose = 1000
    if (len(firstStage) > 1000):
        numToChoose = int(len(firstStage)*0.7)
    firstStage.sort(key=lambda g: g.totalCalls, reverse=True)
    topGenes = list()
    for i in range(0, numToChoose):
        topGenes.append(firstStage[i + 100])
    return topGenes

def calculateConnections(topGenes):
    matrix = [[0 for i in range(len(topGenes))] for j in range(len(topGenes))]
    for i in range(0, len(topGenes)):
        matrix[i] = list(topGenes[i].d.values())
    i = len(matrix[0])
    correlations = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            correlations[i][j] = pearsonr(matrix[i], matrix[j])[0]
    file = open(path +"connections5.4.csv", "w")

    for i in range(len(correlations)):
        for j in range(len(correlations)):
            file.write(str(i+1) + ",")
            file.write(str(j + 1) + ",")
            file.write(str(correlations[i][j]) + "\n")
    file.close()

    return correlations


a1 = [0, 0, 5, 6, 3, 2.3]
a2 = [5, 0, 8, 9, 0,2.6]
a3 = pearsonr(a1,a2)
names = {"old_DBA", "young_DBA"}
numOfCells = {278, 275}
#for i in range (0, len(names)):
calls = pd.read_csv(path + "datasets\\GSE59114\\old_DBA_log.csv" )
calls = calls.iloc[:, :-1] #remove first column of df
#find most important genes
topGenes = findImportantGenes(278, calls)
correlations = calculateConnections(topGenes)

print ("b")



