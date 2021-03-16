import re
import matplotlib
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import os
import glob


# Help methods
def getNumbers(string):
    array = re.findall(r'[0-9]+', string)
    return array


def listToString(s):
    # initialize an empty string
    string_tmp = " "
    return string_tmp.join(s)


# Method that compute the parsing of the file txt extracted from the prompt log
def parser_txt():
    GT = []
    Pred = []
    Count = []
    with open('eval.txt', 'r') as eval_result:
        for line in eval_result:
            firstres = line.rfind("{")
            lastres = line.find("{")
            firstres2 = line.rfind("}")
            lastres2 = line.find("}")
            gt = line[lastres:lastres2 + 1]
            pred = line[firstres:firstres2 + 1]
            allCount = getNumbers(line)
            count = allCount[0:1]
            count = listToString(count)
            GT.append(gt)
            Pred.append(pred)
            Count.append(count)
    GT_final = GT[5:len(GT) - 1]
    Pred_final = Pred[5:len(Pred) - 1]
    Count_final = Count[5:len(Count) - 1]
    Count_final = [int(i) for i in Count_final]
    return GT_final, Pred_final, Count_final


# Method to create the two lists GT and PRED with the  number of occurencies found
def create_matrix_list(GT, Pred, Count):
    Ground_truth = []
    Prediction = []
    for (index, item) in enumerate(Count):
        Ground_truth.extend(GT[index] for x in range(item))
        Prediction.extend(Pred[index] for x in range(item))
    return Ground_truth, Prediction


# Method to create the confusion matrix starting from the lists of Ground Truth and Predict values
def create_Matrix(GT_Matrix, Pred_Matrix):
    # CREATE A DICTIONARY WITH THE TWO LISTS
    data = {
        'y_Actual': GT_Matrix,
        'y_Predicted': Pred_Matrix
    }

    norm = matplotlib.colors.Normalize(0, 1)
    # create the palette for the confusion matrix
    colors = [[norm(0), "#F0FFFF"],
              [norm(0.3), "#82CAFA"],
              [norm(0.6), "#1589FF"],
              [norm(0.8), "blue"],
              [norm(1.0), "darkblue"]]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    df = pd.DataFrame(data, columns=['y_Actual', 'y_Predicted'])
    # set the frequency to 1 to display each value of the lists
    df['frequency'] = 1
    # compute the cross tabulation
    matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])
    sn.set(font_scale=0.7)
    # create the heatmap from the cross tabulation
    sn.heatmap(matrix, annot=True, cmap=cmap, fmt='g', linewidths=.5)
    plt.show()


# method that counts the number of occurence of a letter inside the Ground-Truth
def character_counter(path, letter):
    path = path + r"\Testset"
    print(path)
    # filtering only '.gt.txt' files that we require
    txt_files = glob.glob(path + "/*.gt.txt")
    char_count = 0
    for files in txt_files:
        tmp_file = open(files)
        text = tmp_file.read()
        # count the number of times we find the letter in the sentece
        count = text.count(letter)
        char_count = char_count + count
    # number of times the letter can be found in all sentences
    print(char_count)
    return char_count
