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

distance = [];
testDataSet = [];
finalResult = [];
completeDataSet = []; # used to compare and test accuracy

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
    trainingDataSet = [];
    K = 3;
    K_lowest_distances = [None] * (K);
    index = 0;
    with open('data.csv') as csvfile:
        data_set = csv.reader(csvfile, delimiter=",")

        next(data_set) #skips the first row which are just labels for each column
        #populates tuple with only usable data
        for col in data_set:
            completeDataSet.append([int(col[0]), col[1], float(col[2]), float(col[3]), float(col[6])]);

            if index == 0 or index == 100 or index == 200 or index == 300 or index == 400 or index == 500:
                testDataSet.append([int(col[0]), col[1], float(col[2]), float(col[3]), float(col[6])]);
            else:
                trainingDataSet.append( [int(col[0]), col[1], float(col[2]), float(col[3]), float(col[6])] );

            index = index + 1;

    csvfile.close();


    length_tranining_set = len(trainingDataSet);
    length_testing_set = len(testDataSet);

    for i in range(0, length_testing_set):
        for j in range(0, length_tranining_set):
            if i != j:
                #the distance list contains the two training
                distance.append( [testDataSet[i][0], trainingDataSet[j][0], findDistance(float(testDataSet[i][2]), float(trainingDataSet[j][2]),
                                                                                             float(testDataSet[i][3]), float(trainingDataSet[j][3]),
                                                                                             float(testDataSet[i][4]), float(trainingDataSet[j][4])
                                                                                            )
                                 ]

                               )

        #sort the K number of distances in descending order
         #distance[2].sort();
    #
    #     for counter in range(0, K):
    #         K_lowest_distances[counter] = distance[counter];
    #
    #
    #     testDataSet[i].append(K_lowest_distances);
    #
    # #Loops through the entire list to calculate a label
    # for i in range(0, K):
    #     num_malignant = 0;
    #     num_benign = 0;
    #     #loop through K number of shortest distance
    #     #for j in range(0, K):
    #
    #
    # #    id =              row[0]
    # #    diagnosis =       row[1]
    # #    radius_mean =     row[2]
    # #    texture_mean =    row[3]
    # #    smoothness_mean = row[6]
    #
    #
print(distance[0][2]);