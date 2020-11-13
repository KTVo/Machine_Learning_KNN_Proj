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
import random

import numpy as np
import matplotlib.pyplot as plt

distance = [];
testDataSet = [];
finalResult = [];
completeDataSet = []; # used to compare and test accuracy

X


def get_distance(distance):
    return distance.get('distance');

def findDistance(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z1-z2)*(z1-z2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #    id =              col[0]
    #    diagnosis =       col[1]
    #    radius_mean =     col[2]
    #    texture_mean =    col[3]
    #    smoothness_mean = col[6]


    # structure holding (int id), (char diagnosis), (float radius_mean), (float texture_mean), (float smoothness_mean)
    trainingDataSet = [];
    K = 6;
    K_lowest_distances = [];

    with open('data.csv') as csvfile:
        data_set = csv.reader(csvfile, delimiter=",")

        next(data_set) #skips the first row which are just labels for each column
        #populates tuple with only usable data
        for col in data_set:
            completeDataSet.append({'id': int(col[0]), 'diagnosis': col[1], 'radius_mean': float(col[2]),
                                    'texture_mean': float(col[3]), 'smoothness_mean': float(col[6])});

            if random.randint(0, 1000) < 50:
                testDataSet.append({'id': int(col[0]), 'diagnosis': col[1], 'radius_mean': float(col[2]),
                                    'texture_mean': float(col[3]), 'smoothness_mean': float(col[6])});
            else:
                trainingDataSet.append({'id': int(col[0]), 'diagnosis': col[1], 'radius_mean': float(col[2]),
                                        'texture_mean': float(col[3]), 'smoothness_mean': float(col[6])});


    csvfile.close();

    #setting up and generating 3D graph to plot
    fig = plt.figure();
    ax = fig.gca(projection='3d');

    #setting up colors for scatter plot data
    colors = ('r', 'g', 'b', 'k')

    np




    length_tranining_set = len(trainingDataSet);
    length_testing_set = len(testDataSet);

    for i in range(0, length_testing_set):      #outer loop through all testing points
        for j in range(0, length_tranining_set): #inner loop finds distances betwen a testing point with all training points
            if i != j:

                #the distance list contains the two training
                distance.append({'id_point_test': testDataSet[i].get('id'), 'id_point_train': trainingDataSet[j].get('id'),
                                 'actual_diagnosis_from_training': trainingDataSet[j].get('diagnosis'),
                                  'distance': findDistance(float(testDataSet[i].get('radius_mean')), float(trainingDataSet[j].get('radius_mean')),
                                                           float(testDataSet[i].get('texture_mean')), float(trainingDataSet[j].get('texture_mean')),
                                                           float(testDataSet[i].get('smoothness_mean')), float(trainingDataSet[j].get('smoothness_mean'))
                                                          )
                                  },

                               )


        # sort the of one testingDataSet distances in descending order
        distance.sort(key=get_distance);
        for countTopK in range(0, K):
            K_lowest_distances.append(distance[countTopK]);

        #print(K_lowest_distances);
        distance.clear();
    for i in range(0, len(K_lowest_distances)-1):
        if(i%K == 0):
            finalResult.append({'info': K_lowest_distances[i:i+K], 'predicted_diagnosis': None});
            i = i + K + 1


    print(finalResult[0].get('info')[2].get('actual_diagnosis_from_training') );
    for i in range(0, len(finalResult)):
        num_malignant = 0;
        num_benign = 0;

        for k in range(0, K): #loops through all the 'actual_diagnosis_from_training'
            print(finalResult[i].get('info')[k]);
            if finalResult[i].get('info')[k].get('actual_diagnosis_from_training') == 'M':
                num_malignant = num_malignant + 1;
            elif finalResult[i].get('info')[k].get('actual_diagnosis_from_training') == 'B':
                num_benign = num_benign + 1;

        print("num_malignant = ", num_malignant, " num_benign = ", num_benign);

        if num_malignant > num_benign:
            updatePredictedDiagnosisToMalignant = {'predicted_diagnosis': 'M'}
            finalResult[i].update(updatePredictedDiagnosisToMalignant);
        else:
            updatePredictedDiagnosisToBenign = {'predicted_diagnosis': 'B'}
            finalResult[i].update(updatePredictedDiagnosisToBenign);

        num_of_correct_predictions = 0;
        num_of_wrong_predictions = 0;
        for i in range(0, len(finalResult)):
            for k in range(0, len(completeDataSet)):
                if finalResult[i].get('info')[0].get('id_point_test') == completeDataSet[k].get('id'):
                    print(finalResult[i].get('info')[0].get('id_point_test'), ' == ', completeDataSet[k].get('id'));
                    if finalResult[i].get('predicted_diagnosis') == completeDataSet[k].get('diagnosis'):
                        print("is predictedCORRECT!");
                        print("Predicted Diagnosis = ", finalResult[i].get('predicted_diagnosis'),
                              " Actual Diagnosis = ", completeDataSet[k].get('diagnosis'));
                        num_of_correct_predictions = num_of_correct_predictions + 1;
                        break;
                    else:
                        print("is predicted WRONG!");
                        num_of_wrong_predictions = num_of_wrong_predictions + 1;
                        print("Predicted Diagnosis = ", finalResult[i].get('predicted_diagnosis'),
                              " Actual Diagnosis = ", completeDataSet[k].get('diagnosis'));
                        break;

        print("Correct Prediction Rate: ", num_of_correct_predictions / len(testDataSet), ", Number of Correct Predictions: ", num_of_correct_predictions,
              ", Number of Wrong Predictions:", len(testDataSet));
