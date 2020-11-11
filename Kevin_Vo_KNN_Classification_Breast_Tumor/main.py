#Name:          Kevin Vo
#Student ID:    006316930
#Professor:     Dr. Yan Zhang
#Course:        CSE 5160 (Machine Learning)
#Assignment:    CSE 5160 Machine Learning Course Project

#Description:   This assignment will used the KNN (K-Nearest Neighbors) Algorithm to classify existing breast tumors
#               as malignant or benign based on a data set that was gathered from the source below. In this case, we'll
#               use vales from the mean_smoothness, mean_texture, and radius from the given data set. Within this data set
#               most of the values will be used as the training set were some will be extracted to only be used a the
#               testing set.

#Source of Data Set: https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

#Date:          11/11/2020



import csv
import math

from collections import namedtuple #is used to form a structure to associate piece of data with an x and y component, distance value, and label
DataPointStruct = namedtuple("DataPointStruct", "x y distance label");
arrDataPointStruct = [DataPointStruct];

def findDistance(x, y):
    return math.sqrt((x-y)*(x-y) + (x-y)*(x-y))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

#    id =              row[0]
#    dianosis =        row[1]
#    readius_mean =    row[2]
#    texture_mean =    row[3]
#    smoothness_mean = row[6]

    indx = 0;
    with open('data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")

        for row in readCSV:
            distance = findDistance(row[2], row[6])
            dataPoint = DataPointStruct(row[2], row[6], distance)
            arrDataPointStruct[i] = DataPointStruct;
            i = i + 1;

    for cnt in arrDataPointStruct:
        print(arrDataPointStruct[cnt]);
