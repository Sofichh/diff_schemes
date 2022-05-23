import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def func(uu_, uu, t, h):
    y = (uu + uu_) / 2 + t * (uu_ - uu) / 2 / h
    return y


def analit(time):
    return [1 if (0.1 + time <= x[i] <= 0.2 + time) else 0 for i in range(n+1)]


newu = []
for n in [100, 200, 500, 1000, 2000, 5000, 10000]:
    x = np.linspace(0, 1, n + 1)
    ulist = [1 if (0.1 <= x[i] <= 0.2) else 0 for i in range(n + 1)]
    print(ulist)
    u = np.array(ulist)
    tmax = 0.5
    tt = 0
    xstep = 1 / n
    time_step = 0.8 / n
    while tt <= tmax:
        tt += time_step
        for k in range(0, n):
            if k == n-1:
                newu.append(func(u[k], 0, time_step, xstep))
            else:
                newu.append(func(u[k], u[k+2], time_step, xstep))
        newu.insert(0, 0)
        u = newu
        newu = []
    u_an = analit(tmax)
    plt.grid()
    plt.title("Численное и аналитическое решения в момент времени Т=0.5")
    plt.xlabel("x")
    plt.ylabel("u")
    plt.plot(x, u, x, u_an)
    plt.show()
