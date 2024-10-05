# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_PATH = "..\Data\Obesity_Dataset.xlsx"
SHEET_NAME = "Sheet1"

def make_dataset(filepath):
    data = pd.read_excel(filepath, sheet_name=SHEET_NAME)
    return data.dropna()


if __name__ == '__main__':
    data = make_dataset((FILE_PATH))
    classes = data.columns
    n_col = data.shape[1]
    
    palette = ['green', 'yellow', 'orange', 'red']
    colors = [palette[data.Class[i]-1] for i in range(data.shape[0])]
    varx = np.random.rand(1, data.shape[0])*10**-.5
    vary = np.random.rand(1, data.shape[0])*10**-.5
    
    _, P = plt.subplots(n_col, n_col, figsize=(40, 30))
    for (i, class1) in enumerate(classes[:]):
        for (j, class2) in enumerate(classes[i:]):
            j += i
            x = np.array(data[class1])+varx
            y = np.array(data[class2])+vary
            P[i, j].scatter(x, y, c=colors, s=.7)
            P[j, i].scatter(y, x, c=colors, s=.7)




