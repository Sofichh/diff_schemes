import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def func(uu_, uu, t, h):
    y = uu + t * (uu_ - uu) / h
    return y


def analit(time):
    return [1 if (0.1 + time <= x[i] <= 0.2 + time) else 0 for i in range(n)]


newu = []
for n in [100, 200, 500, 1000, 2000, 5000, 10000]:
    x = np.linspace(1/n, 1, n)
    ulist = [1 if (0.10 <= x[i] <= 0.20) else 0 for i in range(n)]
    print(ulist)
    u = np.array(ulist)
    tmax = 0.5
    tt = 0
    time_step = 0.8 / n
    xstep = 1 / n
    while tt < tmax:
        tt += time_step
        for k in range(0, n-1):
            newu.append(func(u[k], u[k+1], time_step, xstep))
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

