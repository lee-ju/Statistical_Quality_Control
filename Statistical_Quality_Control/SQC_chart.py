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

def p_chart(D, n, var='pi'):
    p = D[var].values
    pbar = p.mean()
    
    UCL = pbar + 3 * np.sqrt(pbar * (1 - pbar) / n)
    LCL = pbar - 3 * np.sqrt(pbar * (1 - pbar) / n)
    if LCL < 0:
        LCL = 0

    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(p,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(pbar,
            linestyle='dashed', color='blue')
    ax.set_title(r'p chart')
    ax.set(xlabel='Sample number',
           ylabel='Sample fraction nonconforming, $\^p$')
    return round(pbar, 4), round(UCL, 4), round(LCL, 4)

def np_chart(D, n, var='pi'):
    p = D[var].values
    pbar = p.mean()
    
    UCL = n * pbar + 3 * np.sqrt(n * pbar * (1 - pbar))
    LCL = n * pbar - 3 * np.sqrt(n * pbar * (1 - pbar))
    
    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(n * p,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
            linestyle='dashed', color='red')
    ax.axhline(LCL,
            linestyle='dashed', color='red')
    ax.axhline(n * pbar,
            linestyle='dashed', color='blue')
    ax.set_title(r'np chart')
    ax.set(xlabel='Sample number',
           ylabel='Sample fraction nonconforming, $\^p$')
    return round(n * pbar, 4), round(UCL, 4), round(LCL, 4)

def c_chart(D, var='N'):
    c = D[var].values
    N = D.shape[0]

    cbar = np.sum(c)/N
    UCL = cbar + 3 * np.sqrt(cbar)
    LCL = cbar - 3 * np.sqrt(cbar)

    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(c,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
               linestyle='dashed', color='red')
    ax.axhline(LCL,
               linestyle='dashed', color='red')
    ax.axhline(cbar,
               linestyle='dashed', color='blue')
    ax.set_title(r'c chart')
    ax.set(xlabel='Sample number',
           ylabel='Number of nonconformities')
    return round(cbar, 4), round(UCL, 4), round(LCL, 4)

def u_chart(D, n, var='avg_err'):
    u = D[var].values
    ubar = u.mean()

    UCL = ubar + 3 * np.sqrt(ubar / n)
    LCL = ubar - 3 * np.sqrt(ubar / n)
    if LCL < 0:
        LCL = 0

    fig, ax = plt.subplots(figsize=(fig0, fig1))
    ax.plot(u,
            linestyle='-', marker='o', color='black')
    ax.axhline(UCL,
               linestyle='dashed', color='red')
    ax.axhline(LCL,
               linestyle='dashed', color='red')
    ax.axhline(ubar,
               linestyle='dashed', color='blue')
    ax.set_title(r'u chart')
    ax.set(xlabel='Sample number',
           ylabel='Error/unit')
    return round(ubar, 4), round(UCL, 4), round(LCL, 4)

if __name__ == '__main__':
    # - - Control Charts for Variables
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from Statistical_Quality_Control import SQC_chart

    D = pd.read_csv('.../Wafer0.csv')
    # Xbar-R Chart
    xR_M, xR_UCL, xR_LCL = SQC_chart.xbar_R_chart(D=D, A2=0.577)
    print(xR_M, xR_UCL, xR_LCL)
    
    # R Chart
    R_R, R_UCL, R_LCL = SQC_chart.R_chart(D, D3=0, D4=2.114)
    print(R_R, R_UCL, R_LCL)
    
    # Xbar-s Chart
    xs_M, xs_UCL, xs_LCL = SQC_chart.xbar_s_chart(D=D, A3=1.427)
    print(xs_M, xs_UCL, xs_LCL)
    
    # s Chart
    s_s, s_UCL, s_LCL = SQC_chart.s_chart(D, B3=0, B4=2.089)
    print(s_s, s_UCL, s_LCL)
    
if __name__ == '__main__':
    # - - Control Charts for Attributes
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from Statistical_Quality_Control import SQC_chart

    D = pd.read_csv('.../Orange0.csv')
    # p Chart
    pbar, p_UCL, p_LCL = SQC_chart.p_chart(D=D, n=50, var='pi')
    print(pbar, p_UCL, p_LCL)

    # np Chart
    npbar, np_UCL, np_LCL = SQC_chart.np_chart(D=D, n=50, var='pi')
    print(npbar, np_UCL, np_LCL)
    
    D = pd.read_csv('.../Chain0.csv')
    # c Chart
    cbar, c_UCL, c_LCL = SQC_chart.c_chart(D=D, var='N')
    print(cbar, c_UCL, c_LCL)

    # u Chart
    ubar, u_UCL, u_LCL = SQC_chart.u_chart(D=D, n=50, var='avg_err')
    print(ubar, u_UCL, u_LCL)
