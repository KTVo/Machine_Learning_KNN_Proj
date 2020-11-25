#Name:          Kevin Vo
#Student ID:    006316930
#Professor:     Dr. Yan Zhang
#Course:        CSE 5160 (Machine Learning)
#Assignment:    CSE 5160 Machine Learning Course Project

#Description:   This assignment will used the KNN (K-Nearest Neighbors) Algorithm to classify existing breast tumors
#               as malignant or benign based on a data set that was gathered from the source below. In this case, we'll
#               use vales from the mean_smoothness, mean_texture, and radius from the given data set. Within this data set
#               most of the values will be used as the training set were some will be extracted to only be used as the
#               testing set.

#Source of Data Set: https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

#Date:          11/11/2020

import csv
import math
import random
import matplotlib.pyplot as plt

#setting up graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

distance = [];              #Stores the distances
testDataSet = [];           #Stores all data for the testing
finalResult = [];

trainingSetB_radius_x = [];  # training set  B: -, Blue
trainingSetB_smooth_y = [];  # training set  B: -, Blue
trainingSetB_texture_z = [];  # training set  B: -, Blue

trainingSetM_radius_x = [];  # training set  M: +, Blue
trainingSetM_smooth_y = [];  # training set  M: +, Blue
trainingSetM_texture_z = [];  # training set  M: +, Blue

testingSetB_radius_x = [];  # training set  B: -, Red
testingSetB_smooth_y = [];  # training set  B: -, Red
testingSetB_texture_z = [];  # training set  B:-+, Red

testingSetM_radius_x = [];  # training set  M: +, Red
testingSetM_smooth_y = [];  # training set  M: +, Red
testingSetM_texture_z = [];  # training set  M: +, Red

# structure holding (int id), (char diagnosis), (float radius_mean), (float texture_mean), (float smoothness_mean)
trainingDataSet = [];
K = 5;
K_lowest_distances = [];
total_num_of_data = 0;


def get_distance(distance):
    return distance.get('distance');


def normalization(subDataSet):
    min = subDataSet.min();
    max = subDataSet.max();
    sizeOfDataSet = len(subDataSet);
    for i in range(0, sizeOfDataSet):
        subDataSet = subDataSet([i] - min)/(max-min);

#find the 3D distance where,
# x1 -> radius means from testDataSet
# x2 -> radius means from trainingDataSet
# y1 -> smoothness means from testDataSet
# y2 -> smoothness means from trainingDataSet
# z1 -> texture means from testDataSet
# z2 -> texture means from trainingDataSet
def findDistance(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z1-z2)*(z1-z2))

#Populates both the testing set and training set
# ~90% of total data entry will go to training set
# the rest of the data entries will go to testing set
# data instances in training set will not appear under testing set and vice versa
def populateLists():

    #    id =              col[0]
    #    diagnosis =       col[1]
    #    radius_mean =     col[2]
    #    texture_mean =    col[3]
    #    smoothness_mean = col[6]

    global total_num_of_data;
    with open('data.csv') as csvfile:
        data_set = csv.reader(csvfile, delimiter=",")

        next(data_set) #skips the first row which are just labels for each column
        #populates tuple with only usable data
        for col in data_set:
            total_num_of_data = total_num_of_data + 1;

            if random.randint(0, 500) < 50:
                testDataSet.append({'id': int(col[0]), 'diagnosis': col[1], 'radius_mean': float(col[2]),
                                    'texture_mean': float(col[3]), 'smoothness_mean': float(col[6])});
                if col[1] == 'M':
                    testingSetM_radius_x.append(float(col[2]))  # training set  M: +, Red
                    testingSetM_smooth_y.append(float(col[6]));  # training set  M: +, Red
                    testingSetM_texture_z.append(float(col[3]));  # training set  M: +, Red
                else:
                    testingSetB_radius_x.append(float(col[2]))  # training set  B: -, Red
                    testingSetB_smooth_y.append(float(col[6]));  # training set  B: -, Red
                    testingSetB_texture_z.append(float(col[3]));  # training set  B: -, Red

            else:
                trainingDataSet.append({'id': int(col[0]), 'diagnosis': col[1], 'radius_mean': float(col[2]),
                                        'texture_mean': float(col[3]), 'smoothness_mean': float(col[6])});

                if col[1] == 'M':
                    trainingSetM_radius_x.append(float(col[2]));  # training set  M: +, Blue
                    trainingSetM_smooth_y.append(float(col[6]));  # training set  M: +, Blue
                    trainingSetM_texture_z.append(float(col[3]));  # training set  M: +, Blue
                else:
                    trainingSetB_radius_x.append(float(col[2]));  # training set  B: -, Blue
                    trainingSetB_smooth_y.append(float(col[6]));  # training set  B: -, Blue
                    trainingSetB_texture_z.append(float(col[3]));  # training set  B: -, Blue
    csvfile.close();



#Calls the findDistance function between a
def getStoreDistance():
    for i in range(0, len(testDataSet)):  # outer loop through all testing points
        for j in range(0, len(trainingDataSet)):  # inner loop finds distances betwen a testing point with all training points
            if i != j:
                # the distance list contains the two training
                distance.append(
                    {'id_point_test': testDataSet[i].get('id'), 'id_point_train': trainingDataSet[j].get('id'),
                     'actual_diagnosis_from_training': trainingDataSet[j].get('diagnosis'),
                     'distance': findDistance(float(testDataSet[i].get('radius_mean')),
                                              float(trainingDataSet[j].get('radius_mean')),
                                              float(testDataSet[i].get('texture_mean')),
                                              float(trainingDataSet[j].get('texture_mean')),
                                              float(testDataSet[i].get('smoothness_mean')),
                                              float(trainingDataSet[j].get('smoothness_mean'))
                                              )
                     },

                    )

        # sort the of one testingDataSet distances in descending order
        distance.sort(key=get_distance);

        for countTopK in range(0, K):
            K_lowest_distances.append(distance[countTopK]);

        # print(K_lowest_distances);
        distance.clear();

    for i in range(0, len(K_lowest_distances) - 1):
        if (i % K == 0):
            finalResult.append({'info': K_lowest_distances[i:i + K], 'predicted_diagnosis': None});
            i = i + K + 1

#Calculates the predicted values of each testing instance then assigns it
def calculatePrediction():
    for i in range(0, len(finalResult)):
        num_malignant = 0;
        num_benign = 0;

        for k in range(0, K):  # loops through all the 'actual_diagnosis_from_training'
            if finalResult[i].get('info')[k].get('actual_diagnosis_from_training') == 'M':
                num_malignant = num_malignant + 1;
            elif finalResult[i].get('info')[k].get('actual_diagnosis_from_training') == 'B':
                num_benign = num_benign + 1;

        if num_malignant > num_benign:
            updatePredictedDiagnosisToMalignant = {'predicted_diagnosis': 'M'}
            finalResult[i].update(updatePredictedDiagnosisToMalignant);
        else:
            updatePredictedDiagnosisToBenign = {'predicted_diagnosis': 'B'}
            finalResult[i].update(updatePredictedDiagnosisToBenign);

#Calculates the accuracy of the predict results then display predicted results individually
#along with displaying the evulation details of the KNN for taht run
def displayTextResults():
    num_of_correct_predictions = 0;
    num_of_wrong_predictions = 0;
    print("\nPrediction Results for All Testing Inputs:\n\tLet K =", K,"\n")
    for i in range(0, len(finalResult)):
        print('Test Input#', i + 1, ' -> ID: ', finalResult[i].get('info')[0].get('id_point_test'), ' -> ', end=" ");
        if finalResult[i].get('predicted_diagnosis') == finalResult[i].get('info')[0].get(
                'actual_diagnosis_from_training'):
            print("was predicted CORRECTLY!");
            print("Predicted Diagnosis = ", finalResult[i].get('predicted_diagnosis'),
                  " Actual Diagnosis = ", finalResult[i].get('info')[0].get('actual_diagnosis_from_training'), '\n');
            num_of_correct_predictions = num_of_correct_predictions + 1;
        else:
            print("was predicted WRONG!");
            num_of_wrong_predictions = num_of_wrong_predictions + 1;
            print("Predicted Diagnosis = ", finalResult[i].get('predicted_diagnosis'),
                  " Actual Diagnosis = ", finalResult[i].get('info')[0].get('actual_diagnosis_from_training'), '\n');

    print("\tEvaluation of the KNN ==> For K =", K, ":\n\t\tCorrect Prediction Rate:",
          "{:.2f}".format((num_of_correct_predictions / len(testDataSet))*100) + "%",
          "\n\t\tNumber of Correct Predictions:",
          num_of_correct_predictions, "\n\t\tTotal Size of Testing Set:", len(testDataSet),
          "\n\t\tTotal Size of Entire Data Set:", total_num_of_data);

    print("\nLabel Definitions for the scatter plot:");
    print("\tRed  -> A point from the Testing Set\n\tBlue -> A point from the Training Set\n\t+    -> Malignant Tumor" +
          "\n\t-    -> Benign Tumor");

#Generates 3D-scatter plot
def displayGraph():
    ax.scatter(trainingSetB_radius_x, trainingSetB_smooth_y, trainingSetB_texture_z, c='b', marker='_');

    ax.scatter(trainingSetM_radius_x, trainingSetM_smooth_y, trainingSetM_texture_z, c='b', marker='+');

    ax.scatter(testingSetB_radius_x, testingSetB_smooth_y, testingSetB_texture_z, c='r', marker='_');

    ax.scatter(testingSetM_radius_x, testingSetM_smooth_y, testingSetM_texture_z, c='r', marker='+');

    ax.set_xlabel('radius_mean')
    ax.set_ylabel('smoothness_mean')
    ax.set_zlabel('texture_mean')

    ax.set_zlim(0, 25.0);

    plt.xlim(0, 22.0);
    plt.ylim(0.09, 0.18);

    plt.show();


#The main calling all the other functions
if __name__ == '__main__':
    populateLists();       #populates all the lists

    getStoreDistance();    #calculate then store the distances

    calculatePrediction(); #Calculate then store the predicted outcome for each testing instance w/in testing set

    displayTextResults();  #Display relevant results of the prediction along with algo. evulation details

    displayGraph();        #Generates 3D-scatter plot graph based on the KNN classification algo.
