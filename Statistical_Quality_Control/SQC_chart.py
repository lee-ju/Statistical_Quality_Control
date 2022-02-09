import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

fig0 = 10
fig1 = 5
def xbar_R_chart(D, A2):
    m = D.shape[0]
    x_bar = []
    r = []
    for i in range(m):
        mi = D.iloc[i, 1:].values
        x_bar.append(mi.mean())
        r.append(mi.max() - mi.min())

    x_barbar = np.mean(x_bar)
    r_bar = np.mean(r)
    UCL = x_barbar + A2 * r_bar
    LCL = x_barbar - A2 * r_bar

    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(x_bar,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(x_barbar,
            linestyle='dashed', color='blue')
    ax.set_title(r'$\barX$ chart')
    ax.set(xlabel='Group', ylabel='Average')
    return round(x_barbar, 4), round(UCL, 4), round(LCL, 4)

def R_chart(D, D3, D4):
    m = D.shape[0]
    r = []
    for i in range(m):
        mi = D.iloc[i, 1:].values
        r.append(mi.max() - mi.min())

    r_bar = np.mean(r)
    UCL = D4 * r_bar
    LCL = D3 * r_bar

    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(r,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(r_bar,
            linestyle='dashed', color='blue')
    ax.set_title('R chart')
    ax.set(xlabel='Group', ylabel='Range')
    return round(r_bar, 4), round(UCL, 4), round(LCL, 4)

if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from Statistical_Quality_Control import SQC_chart
    D = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Data/Wafer0.csv')
    xR_M, xR_UCL, xR_LCL = SQC_chart.xbar_R_chart(D=D, A2=0.577)
    print(xR_M, xR_UCL, xR_LCL)
    
    R_R, R_UCL, R_LCL = SQC_chart.R_chart(D, D3=0, D4=2.114)
    print(R_R, R_UCL, R_LCL)
