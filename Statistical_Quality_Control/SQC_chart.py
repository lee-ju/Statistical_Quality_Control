import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

def xbar_chart(D, A2):
    m = D.shape[0]
    x_bar = []
    R = []
    for i in range(m):
        mi = D.iloc[i, 1:].values
        x_bar.append(mi.mean())
        R.append(mi.max() - mi.min())

    M = np.mean(x_bar)
    UCL = M + A2 * np.mean(R)
    LCL = M - A2 * np.mean(R)

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

def R_chart(D, D3, D4):
    m = D.shape[0]
    R = []
    for i in range(m):
        mi = D.iloc[i, 1:].values
        R.append(mi.max() - mi.min())

    Rbar = np.mean(R)
    UCL = D4 * Rbar
    LCL = D3 * Rbar

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(R,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(Rbar,
            linestyle='dashed', color='blue')
    ax.set_title('R chart')
    ax.set(xlabel='Group', ylabel='Range')
    return round(Rbar, 4), round(UCL, 4), round(LCL, 4)

if __name__ == '__main__':
    from Statistical_Quality_Control import SQC_chart
    D = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Data/Wafer0.csv')
    xbar_M, xbar_UCL, xbar_LCL = SQC_chart.xbar_chart(D=D, A2=0.577)
    print(xbar_M, xbar_UCL, xbar_LCL)
    
    R_Rbar, R_UCL, R_LCL = R_chart(D, D3=0, D4=2.114)
    print(R_Rbar, R_UCL, R_LCL)
