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
    ax.set_title(r'$\barX$-R chart')
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

def xbar_s_chart(D, A3):
    m = D.shape[0]
    x_bar = []
    s = []
    for i in range(m):
        mi = D.iloc[i, 1:].values
        x_bar.append(mi.mean())
        s.append(mi.std())

    x_barbar = np.mean(x_bar)
    s_bar = np.mean(s)
    UCL = x_barbar + A3 * s_bar
    LCL = x_barbar - A3 * s_bar

    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(x_bar,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(x_barbar,
            linestyle='dashed', color='blue')
    ax.set_title(r'$\barX$-s chart')
    ax.set(xlabel='Group', ylabel='Average')
    return round(x_barbar, 4), round(UCL, 4), round(LCL, 4)

def s_chart(D, B3, B4):
    m = D.shape[0]
    s = []
    for i in range(m):
        mi = D.iloc[i, 1:].values
        s.append(mi.std())

    s_bar = np.mean(s)
    UCL = B4 * s_bar
    LCL = B3 * s_bar

    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(s,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(s_bar,
            linestyle='dashed', color='blue')
    ax.set_title('s chart')
    ax.set(xlabel='Group', ylabel='Range')
    return round(s_bar, 4), round(UCL, 4), round(LCL, 4)

if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    D = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Data/Wafer0.csv')
    
    # Xbar-R Chart
    xR_M, xR_UCL, xR_LCL = xbar_R_chart(D=D, A2=0.577)
    print(xR_M, xR_UCL, xR_LCL)
    
    # R Chart
    R_R, R_UCL, R_LCL = R_chart(D, D3=0, D4=2.114)
    print(R_R, R_UCL, R_LCL)
    
    # Xbar-s Chart
    xs_M, xs_UCL, xs_LCL = xbar_s_chart(D=D, A3=1.427)
    print(xs_M, xs_UCL, xs_LCL)
    
    # s Chart
    s_s, s_UCL, s_LCL = s_chart(D, B3=0, B4=2.089)
    print(s_s, s_UCL, s_LCL)
