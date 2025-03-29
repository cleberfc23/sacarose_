import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_graph(data, title= ""):
    plt.plot(data.values)
    plt.title(title)
    plt.grid()
    print("plot graph")

