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
import sys #for getting the max value for a float
from struct import *    #imports from all



from collections import namedtuple #is used to form a structure to associate piece of data with an x and y component, distance value, and label
DataPointStruct = namedtuple("DataPointStruct", "x y distance label");
arrDataPointStruct = [DataPointStruct];

def findDistance(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z1-z2)*(z1-z2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #    id =              row[0]
    #    diagnosis =       row[1]
    #    radius_mean =     row[2]
    #    texture_mean =    row[3]
    #    smoothness_mean = row[6]


    # structure holding (int id), (char diagnosis), (float radius_mean), (float texture_mean), (float smoothness_mean)
    tupleUsableData = [];
    max_value_of_float = sys.float_info.max;
    K = 3;
    K_lowest_distances = [];
    for i in range(0, K):
        K_lowest_distances.append( max_value_of_float );

    with open('data.csv') as csvfile:
        data_set = csv.reader(csvfile, delimiter=",")

        next(data_set) #skips the first row which are just labels for each column
        #populates tuple with only usable data
        for col in data_set:
            tupleUsableData.append( ([ col[0], col[1], float(col[2]), float(col[3]), float(col[6])]) );

    #print(tupleUsableData[0][2]);
    csvfile.close();


    length = len(tupleUsableData) - 1;

    #Calculate the distance between a data entry and all other data entries for each entry
    indx = 0;
    for col in range(0, length):
        for innerCol in range(0, length):
            if(tupleUsableData[col][0] != tupleUsableData[innerCol][0]):
                distance = findDistance( float(tupleUsableData[col][2]), float(tupleUsableData[innerCol][2]),
                                         float(tupleUsableData[col][3]), float(tupleUsableData[innerCol][3]),
                                         float(tupleUsableData[col][4]), float(tupleUsableData[innerCol][4])
                                      )
                #sort the K number of distances in descending order
                K_lowest_distances.sort(reverse=True);

                for cntIndx in range(0, K):
                    if(K_lowest_distances[cntIndx] > distance):
                        K_lowest_distances[cntIndx] = distance;
                        cntIndx = K;


        tupleUsableData[col].append(K_lowest_distances);



print(tupleUsableData);

