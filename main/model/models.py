import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout


def get_lstm(n_input, n_output):
    """ 
    Title:
    Authors:
    Link:
    """
    
    model = Sequential()
    model.add(LSTM(128,  input_shape=(
        n_input, 1)))
    model.add(Dense(150, activation='relu'))
    model.add(Dropout(0.20))
    model.add(Dense(100, activation='relu'))
    model.add(Dropout(0.15))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(units=n_output, activation='relu'))
    return model