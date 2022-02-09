import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

def xbar_chart(D, thread_val):
    m = D.shape[0]
    x_bar = []
    R = []
    for i in range(m):
        mi = D.iloc[i, 1:].values
        x_bar.append(mi.mean())
        R.append(mi.max() - mi.min())

    M = np.mean(x_bar)
    UCL = M + thread_val * np.mean(R)
    LCL = M - thread_val * np.mean(R)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x_bar,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(M,
            linestyle='dashed', color='blue')
    ax.set_title('X-bar chart')
    ax.set(xlabel='Group', ylabel='Average')
    return round(M, 4), round(UCL, 4), round(LCL, 4)
