import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as MSE,  mean_absolute_error as MAE


def mean_squared_error(y_true, y_predicted):
    return MAE(y_true,y_predicted)