import numpy as np
import pandas as pd
import pickle
import seaborn as sns
from matplotlib import pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

import xgboost as xgb


def predict_CVD(response):
    fileName = 'predict/voting_final.pkl'
    loaded_model = pickle.load(open(fileName, 'rb'))
    age = response['age']
    gender = response['gender']
    height = response['height']
    weight = response['weight']
    ap_hi = response['ap_hi']
    ap_lo = response['ap_lo']
    cholesterol = response['cholesterol']
    gluc = response['gluc']
    smoke = response['smoke']
    alco = response['alco']
    active = response['active']
    years = response['years']
    bmi = weight/((height/100)**2)
    sample = np.array([age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, years, bmi]).reshape(1, -1)
    print()
    pred = loaded_model.predict_proba(sample)
    return pred


# response = {'age': 15799,
#             'gender': 2,
#             'height': 176,
#             'weight': 77.0,
#             'ap_hi': 120,
#             'ap_lo': 80,
#             'cholesterol': 3,
#             'gluc': 3,
#             'smoke': 0,
#             'alco': 0,
#             'active': 1,
#             'years': 23
# }

#89% 
# response = {'age': 7325,
#             'gender': 2,
#             'height': 168,
#             'weight': 62.0,
#             'ap_hi': 110,
#             'ap_lo': 80,
#             'cholesterol': 1,
#             'gluc': 1,
#             'smoke': 0,
#             'alco': 0,
#             'active': 1,
#             'years': 20
# }

response = {'age': 8400,
            'gender': 1,
            'height': 163,
            'weight': 45.0,
            'ap_hi': 110,
            'ap_lo': 80,
            'cholesterol': 1,
            'gluc': 1,
            'smoke': 0,
            'alco': 0,
            'active': 0,
            'years': 23
}

# result =  predict_CVD(response).tolist()
# print("\n\n\nProbability of cardiovascular disease is: ", str(round(result[0][1],3) * 100) + "%" )
# print("The probability of the absence of cardiovascular disease is: ", str(round(result[0][0],3) * 100) + "%" )